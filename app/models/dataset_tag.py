from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class DatasetTag(Base):
    __tablename__ = "dataset_tag"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("dataset.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tag.id"), nullable=False)
    is_filterable = Column(Boolean, nullable=False, default=False)

    dataset = relationship("Dataset", back_populates="dataset_tags")
    tag = relationship("Tag", back_populates="dataset_tags")

    def __repr__(self):
        return f"<DatasetTag(dataset_id='{self.dataset_id}', tag_id='{self.tag_id}')>"
