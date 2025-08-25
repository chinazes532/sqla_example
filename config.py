from pydantic_settings import BaseSettings
from pydantic import Field, field_validator
from typing import List


class CommonConfig(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


class BotConfig(CommonConfig):
    bot_token: str = Field(..., alias="BOT_TOKEN")
    admins: List[int] = Field(default_factory=list, alias="ADMINS")
    channel_id: int = Field(..., alias="CHANNEL_ID")
    channel_link: str = Field(..., alias="CHANNEL_LINK")


class RedisConfig(CommonConfig):
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")


class DatabaseConfig(CommonConfig):
    database_url: str = Field(default="sqlite+aiosqlite:///database.db", alias="DATABASE_URL")


class Settings:
    bot = BotConfig()
    redis = RedisConfig()
    database = DatabaseConfig()


config = Settings()
