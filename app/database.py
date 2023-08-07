from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from app.config import Settings

settings = Settings()


url = URL.create(
    drivername="postgresql",
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
)

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

asyncpg_url = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
)

async_engine = create_async_engine(asyncpg_url, pool_pre_ping=True, echo=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
