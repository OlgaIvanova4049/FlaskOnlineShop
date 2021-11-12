from pydantic import BaseSettings, PostgresDsn

from app.orm.schemas.core import EnvironmentSchema


class Settings(BaseSettings):
    sqlalchemy_database_uri: PostgresDsn
    environment: EnvironmentSchema
    celery_broker_url: str
    celery_result_backend: str
    algorithm: str
    secret_key: str
    mail_port: int
    smtp_server: str
    mail_password: str
    sender_email: str
    admin_email: str

    def get_original_env(self):
        return {key.upper(): value for key, value in self.dict().items()}


settings = Settings()
