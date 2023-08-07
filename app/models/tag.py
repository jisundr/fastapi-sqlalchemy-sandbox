from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Tag(name='{self.name}')>"
