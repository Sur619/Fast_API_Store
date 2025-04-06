from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "sqlite+aiosqlite:///./db.sqlite"
    echo: bool = False  # print SQL queries to the console


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()
