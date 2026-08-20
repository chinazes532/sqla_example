from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List


class CommonConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class BotConfig(CommonConfig):
    bot_token: Annotated[str, Field(...)]
    channel_id: Annotated[int, Field(...)]
    channel_link: Annotated[str, Field(...)]


class RedisConfig(CommonConfig):
    redis_url: Annotated[str, Field(...)]


class DatabaseConfig(CommonConfig):
    db_name: str = Field(...)
    db_user: str = Field(...)
    db_password: str = Field(...)
    db_host: str = Field(...)
    db_port: int = Field(...)

    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class Settings:
    bot = BotConfig()
    redis = RedisConfig()
    database = DatabaseConfig()


config = Settings()
