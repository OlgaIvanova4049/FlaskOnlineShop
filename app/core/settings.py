from pydantic import BaseSettings, PostgresDsn

from app.orm.schemas.core import EnvironmentSchema


class Settings(BaseSettings):
    sqlalchemy_database_uri: PostgresDsn
    environment: EnvironmentSchema

    def get_original_env(self):
        return {key.upper(): value for key, value in self.dict().items()}


settings = Settings()
