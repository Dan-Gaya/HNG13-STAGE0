import os
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Profile API"
    CAT_FACT_URL: str = "https://catfact.ninja/fact"
    REQUEST_TIMEOUT: float = 5.0
    EMAIL: str = "abdulnurakani@gmail.com"
    FULL_NAME: str = "Abdulaziz Nura Kani"
    STACK: str = "Python/FastAPI"

    # class Config:
    #     env_file = ".env"

settings = Settings()
