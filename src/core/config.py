from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'App title'
    app_version: str = '1.0.0'
    database_url: str = 'postgresql+asyncpg://postgres:postgres@db:5432/fastapi' # noqa
    postgres_db: str = 'fastapi'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    db_host: str = 'db'
    db_port: int = 5432
    secret = 'secret'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
