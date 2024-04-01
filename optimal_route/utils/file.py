import csv
from typing import List

import aiofiles

from optimal_route.schemas import point_schemas


async def read_file(file) -> List[point_schemas.PointSave]:
    csv_data = await file.read()
    decoded_csv_data = csv_data.decode("utf-8")
    reader = csv.DictReader(
        decoded_csv_data.splitlines(), delimiter=",", quotechar="\n"
    )
    return [
        point_schemas.PointSave(
            lat=float(point.get("lat")),
            lng=float(point.get("lng")),
            city=point.get("city"),
        )
        for point in reader
    ]
