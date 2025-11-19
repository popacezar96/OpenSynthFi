from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings  # TODO see if necessary

import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    PG_USER : str = os.getenv("PG_USER")
    PG_PASS = os.getenv("PG_PASS")
    PG_SERVER : str = os.getenv("PG_SERVER", "localhost")
    PG_DB_NAME : str = os.getenv("PG_DB")
    PG_DB_SERVICE : str = os.getenv("PG_DB_SERVICE")
    PG_PORT : str = os.getenv("PG_PORT", 5432)

    # entry point to db
    DATABASE_URL=f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_DB_SERVICE}:{PG_PORT}/{PG_DB_NAME}"


settings = Settings()