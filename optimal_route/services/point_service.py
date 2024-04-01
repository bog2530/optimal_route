import uuid

from fastapi import status
from fastapi.exceptions import HTTPException
from optimal_route.schemas import point_schemas
from optimal_route.repository import PointRepository
from optimal_route.utils import read_file, nearest_neighbor
from db.point import Point


class PointServise:
    def __init__(self, point_repository: PointRepository):
        self.point_repo = point_repository

    async def get_router_uuid(self, uuid_router) -> point_schemas.ResponsePoint:
        points = await self.point_repo.get_by_uuid(uuid_router)
        return point_schemas.ResponsePoint(
            id=uuid_router, points=[point_schemas.Point(**point) for point in points]
        )

    async def save_point(self, file) -> point_schemas.ResponsePoint:
        uuid_result = uuid.uuid4()
        points = await read_file(file)
        if points:
            points = nearest_neighbor(points)
            await self.point_repo.save_point(
                [
                    Point(
                        uuid=str(uuid_result),
                        lat=point.lat,
                        lng=point.lng,
                        city=point.city,
                    )
                    for point in points
                ]
            )
            return point_schemas.ResponsePoint(id=uuid_result, points=points)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )
