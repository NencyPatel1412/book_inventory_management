from pydantic import Extra
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config= SettingsConfigDict(extra=Extra.allow, env_file='./.env', env_file_encoding='utf-8')
    DEBUG: bool = False
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    # JWTALGORITHM: str
    # JWTSECRETKEY: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: str

    # GOOGLE_CLIENT_ID: str
    # GOOGLE_CLIENT_SECRET: str
    # GOOGLE_REDIRECT_URI: str
    # GOOGLE_GRANT_TYPE: str

    # MAIL_USERNAME: str
    # MAIL_PASSWORD: str
    # MAIL_FROM: str
    # MAIL_PORT: int
    # MAIL_SERVER: str

    class config:
        env_file = './.env'

setting = Settings()