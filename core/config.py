from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "sqlite+aiosqlite:///./db.sqlite"
    db_echo: bool = True  # print SQL queries to the console


settings = Settings()
