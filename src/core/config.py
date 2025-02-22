import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()


class Settings(BaseSettings):
    DB_URI: str = os.getenv("DB_URI", "mongodb://localhost:27017/dbPulse")
    TIME_INTERVAL: int = os.getenv("TIME_INTERVAL", 10)

settings = Settings()
