from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.dataset_tag import DatasetTag


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("tag_category.id"), nullable=False)

    datasets = relationship(
        "Dataset", secondary=DatasetTag.__tablename__, back_populates="tags"
    )

    tag_category = relationship("TagCategory", back_populates="tags")

    def __repr__(self):
        return f"<Tag(name='{self.name}')>"
