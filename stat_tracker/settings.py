from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DEBUG: bool = True
    TESTING: bool = False
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        env_prefix = "TRACKER_"


settings = Settings()
