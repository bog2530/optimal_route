from typing import List

from optimal_route.schemas import point_schemas


def euclidean_distance(point_1, point_2) -> float:
    return ((point_2.lat - point_1.lat) ** 2 + (point_2.lng - point_1.lng) ** 2) ** 0.5


def nearest_neighbor(
    points: List[point_schemas.PointSave],
) -> List[point_schemas.PointSave]:
    route = [points[0]]
    remaining = set(range(1, len(points)))
    while remaining:
        nearest = min(remaining, key=lambda x: euclidean_distance(route[-1], points[x]))
        route.append(points[nearest])
        remaining.remove(nearest)
    return route
