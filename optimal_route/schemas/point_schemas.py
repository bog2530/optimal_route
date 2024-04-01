from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class Point(BaseModel):
    lat: float
    lng: float


class PointSave(Point):
    city: Optional[str]


class ResponsePoint(BaseModel):
    id: UUID
    points: List[Point]
