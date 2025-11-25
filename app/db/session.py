import os
from sqlmodel import create_engine
from sqlalchemy

DATABASE_URL: str

if not os.getenv("DATABASE_URL"):
    DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_engine(DATABASE_URL)
