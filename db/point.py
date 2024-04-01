from sqlalchemy import Column, Integer, String, Float

from db.base import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    city = Column(String, default=None)
