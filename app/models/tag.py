from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.dataset_tag import DatasetTag


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    datasets = relationship(
        "Dataset", secondary=DatasetTag.__tablename__, back_populates="tags"
    )

    def __repr__(self):
        return f"<Tag(name='{self.name}')>"
