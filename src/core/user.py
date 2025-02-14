from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager,
    FastAPIUsers,
    IntegerIDMixin,
    InvalidPasswordException
)
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.db import get_session
from models.user import User
from schemas.user import UserCreate


async def get_user_db_connection(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)


cookie_transport = CookieTransport(
    cookie_name='znaju_cookie',
    cookie_max_age=300
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret,
                       lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='cookie_backend',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Менеджер пользователей.
    """
    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason=f'Password should be at least {8} characters'
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason='Password should not contain email'
            )

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None
    ) -> None:
        print(f'Пользователь {user.email} зарегистрирован.')


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db_connection)
        ):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)
