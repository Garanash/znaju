from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, String, Text, Integer

from core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    patronymic = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    last_visit = Column(DateTime)
    courses = Column(String)
    birthdate = Column(DateTime)
    expirience = Column(Integer)
    badges = Column(Integer)
    image = Column(String)
    role = Column(String)
    bio = Column(Text)
