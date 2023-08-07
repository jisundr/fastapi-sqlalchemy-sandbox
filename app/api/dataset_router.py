from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, contains_eager
from sqlalchemy.sql import select, and_
from typing import Annotated

from app.dependencies import get_async_db
from app.models import Dataset, DatasetTag, Tag

dataset_router = APIRouter(prefix="/datasets", tags=["Datasets"])


@dataset_router.get("/")
async def get_dataset_list(
    db: Annotated[Session, Depends(get_async_db)],
):
    query = (
        select(Dataset)
        .outerjoin(
            DatasetTag,
            and_(
                Dataset.id == DatasetTag.dataset_id, DatasetTag.is_filterable.is_(True)
            ),
        )
        .options(
            contains_eager(Dataset.dataset_tags)
            .selectinload(DatasetTag.tag)
            .contains_eager(Tag.tag_category)
        )
    )

    result = await db.execute(query)
    datasets = result.unique().scalars().all()
    return datasets
