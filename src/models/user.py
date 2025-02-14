from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, String, Text, Integer

from src.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    patronymic = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    last_visit = Column(DateTime, nullable=False)
    courses = Column(String, nullable=False)
    birthdate = Column(DateTime)
    expirience = Column(Integer, nullable=False)
    badges = Column(Integer, nullable=False)
    image = Column(String, nullable=False)
    role = Column(String, nullable=False)
    bio = Column(Text, nullable=False)
