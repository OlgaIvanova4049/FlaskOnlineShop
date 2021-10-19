from pydantic import BaseSettings, PostgresDsn

from app.orm.schemas.core import EnvironmentSchema


class Settings(BaseSettings):
    sqlalchemy_database_uri: PostgresDsn
    environment: EnvironmentSchema
    # class Config:
    #     env_file = ''


settings = Settings()
