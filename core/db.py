from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import get_settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./social_media_db"
SQLALCHEMY_DATABASE_URL = (
    "postgresql://admin:password@social-network:5432/social_media_db"
)

settings = get_settings()
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
