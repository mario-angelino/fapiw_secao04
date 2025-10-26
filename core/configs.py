from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://postgres.kwruoxeepphdvxdzwksl:c1c2c3c4C5%23@aws-1-us-east-2.pooler.supabase.com:5432/postgres'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')

    class config:
        case_sensitive = True


settings: Settings = Settings()
