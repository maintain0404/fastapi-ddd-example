from enum import Enum

from pydantic import BaseModel, BaseSettings, SecretStr


class DeployMode(str, Enum):
    LOCAL = "local"
    DEVEVLOP = "dev"
    PRODUCTION = "prod"
    STAGE = "stage"


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

    DEPLOY_MODE: DeployMode
    DEBUG: bool
    JWT_SECRET: str
    TIMEZONE: str

    APP_NAME: str
    APP_DESCRIPTION: str


config = Settings()
