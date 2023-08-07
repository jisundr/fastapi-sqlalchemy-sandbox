from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base


class DatasetTag(Base):
    __tablename__ = "dataset_tag"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("dataset.id"))
    tag_id = Column(Integer, ForeignKey("tag.id"))

    def __repr__(self):
        return f"<DatasetTag(dataset_id='{self.dataset_id}', tag_id='{self.tag_id}')>"
