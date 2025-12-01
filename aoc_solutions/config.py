from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aoc_session: str

    class Config:
        env_file = ".env"

settings = Settings()