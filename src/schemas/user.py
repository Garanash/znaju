import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    email: str
    first_name: str
    last_name: Optional[str] = None
    is_active: bool
    last_visit: Optional[datetime.date] = None
    expirience: int = None


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    first_name: str
    last_name: Optional[str] = None
    patronimic: Optional[str] = None
    birthdate: datetime.datetime
    bio: Optional[str] = None


class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    patronimic: Optional[str] = None
    birthdate: Optional[datetime.datetime] = None
    bio: Optional[str] = None
    password: Optional[str] = None
    image: Optional[str] = None
