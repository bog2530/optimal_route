from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, File

from optimal_route.schemas import point_schemas
from optimal_route.services import PointServise
from optimal_route.dependences import point_service

router = APIRouter()


@router.get("/routes/{id}")
async def get_routes(
    id: UUID, point_service: PointServise = Depends(point_service)
) -> point_schemas.ResponsePoint:
    return await point_service.get_router_uuid(id)


# point_schemas.ResponsePoint
@router.post("/routes")
async def get_routes(
    csv: UploadFile = File(...), point_service: PointServise = Depends(point_service)
) -> point_schemas.ResponsePoint:
    return await point_service.save_point(csv)
