import uuid
from typing import List, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.point import Point


class PointRepository:
    _model = Point

    def __init__(self, session: AsyncSession):
        self._session: AsyncSession = session

    async def get_by_uuid(self, uuid_router: uuid) -> List[Type[_model]]:
        stmt = select(self._model).where(self._model.uuid == str(uuid_router))
        result = await self._session.execute(stmt)
        self._session.expunge_all()
        return [point[0].__dict__ for point in result]

    async def save_point(self, data: List[_model]) -> None:
        for point in data:
            self._session.add(point)
