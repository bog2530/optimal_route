from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from starlette.requests import Request

from config import DefaultSettings
from optimal_route.repository import PointRepository
from optimal_route.services import PointServise

settings = DefaultSettings()


def get_engine(request: Request):
    return async_sessionmaker(request.app.db_engine)


async def get_session(engine: async_sessionmaker = Depends(get_engine)) -> AsyncSession:
    async with engine() as session:
        async with session.begin():
            yield session


def point_repo(connection=Depends(get_session)):
    return PointRepository(connection)


def point_service(point_repository=Depends(point_repo)):
    return PointServise(point_repository)
