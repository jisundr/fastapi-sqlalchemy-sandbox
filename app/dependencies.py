from functools import lru_cache
from sqlalchemy.orm import Session

from app.database import async_session
from app.config import Settings


@lru_cache()
def get_settings():
    return Settings()


async def get_async_db():
    async with async_session() as session:
        async with session.begin():
            yield session
