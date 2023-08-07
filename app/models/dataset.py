import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.dataset_tag import DatasetTag


class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    tags = relationship(
        "Tag", secondary=DatasetTag.__tablename__, back_populates="datasets"
    )

    def __repr__(self):
        return f"<Dataset(name='{self.name}', description='{self.description}')>"
