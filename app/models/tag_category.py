from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class TagCategory(Base):
    __tablename__ = "tag_category"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    hex_color = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)

    tags = relationship("Tag", back_populates="tag_category")

    def __repr__(self):
        return f"<TagCategory(name='{self.name}')>"
