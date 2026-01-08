from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel

from .config import settings

# Async engine for the app
engine = create_async_engine(
    settings.database_url_async,
    echo=True,  # set False in production
    future=True,
)

# Async session factory
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


# Optional dev-only helper. In real environments, use Alembic migrations instead.
async def init_db() -> None:
    """Create tables in the database (for local dev / tests).

    NOTE: In real environments prefer to use Alembic migrations instead of this.
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
