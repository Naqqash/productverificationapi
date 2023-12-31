from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    dbUrl: str
    # dbDatabase: str
    # logKey: str
    # JWT_SECRET: str
    # JWT_ALGORITHM: str
    origins: str


class AdminLoginSchema(BaseModel):
    Username: str
    Password: str


settings = Settings()
