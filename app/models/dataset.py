import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from app.models.base import Base
from app.models.dataset_tag import DatasetTag


class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    dataset_tags = relationship("DatasetTag", back_populates="dataset")

    @hybrid_property
    def filterable_dataset_tags(self):
        return [dt for dt in self.dataset_tags if dt.is_filterable]

    def __repr__(self):
        return f"<Dataset(name='{self.name}', description='{self.description}')>"
