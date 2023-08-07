from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.sql import select
from typing import Annotated

from app.dependencies import get_async_db
from app.models import Dataset, Tag

dataset_router = APIRouter(prefix="/datasets", tags=["Datasets"])


@dataset_router.get("/")
async def get_dataset_list(
    db: Annotated[Session, Depends(get_async_db)],
):
    query = select(Dataset).options(
        selectinload(Dataset.tags).selectinload(Tag.tag_category)
    )
    result = await db.execute(query)
    datasets = result.scalars().all()
    return datasets
