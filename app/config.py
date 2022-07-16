from datetime import tzinfo

from common.enum import DeployMode
from pydantic import BaseModel, BaseSettings, SecretStr


class DatabaseSettings(BaseModel):
    DB_TYPE: str  # DB Application name. ex) postgresql, mysql
    HOST: str
    DBAPI: str  # For SQLAlchemy
    NAME: str
    SCHEMA: str | None  # For postgresql
    PORT: int
    USER: str
    PASSWORD: SecretStr

    @property
    def SQLALCHEMY_URI(self):
        return (
            f"{self.DB_TYPE}+{self.DBAPI}://"
            f"{self.HOST}:{self.PORT}@{self.USER}:{self.PASSWORD}/{self.NAME}"
        )


class Settings(BaseSettings):
    READ_DB: DatabaseSettings
    WRITE_DB: DatabaseSettings

    DEPLOY_MODE: DeployMode = DeployMode.LOCAL
    DEBUG: bool
    TIMEZONE: tzinfo

    APP_NAME: str
    APP_DESCRIPTION: str
    APP_HOST: str
    APP_PORT: str


config = Settings()
