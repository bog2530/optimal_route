from optimal_route.utils.retrieval import euclidean_distance, nearest_neighbor


class MockPoint:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


def test_euclidean_distance():
    point1 = MockPoint(0, 0)
    point2 = MockPoint(3, 4)
    assert euclidean_distance(point1, point2) == 5


def test_nearest_neighbor_identical_coordinates():
    points = [MockPoint(0, 0), MockPoint(0, 0), MockPoint(0, 0)]
    route = nearest_neighbor(points)
    assert (
        (route[0].lat == 0 and route[0].lng == 0)
        and (route[1].lat == 0 and route[1].lng == 0)
        and (route[2].lat == 0 and route[2].lng == 0)
    )


def test_nearest_neighbor():
    points = [
        MockPoint(0, 0),
        MockPoint(100, 100),
        MockPoint(10, 10),
        MockPoint(1000, -1000),
    ]
    route = nearest_neighbor(points)
    assert (
        (route[0].lat == 0 and route[0].lng == 0)
        and (route[1].lat == 10 and route[1].lng == 10)
        and (route[2].lat == 100 and route[2].lng == 100)
        and (route[3].lat == 1000 and route[3].lng == -1000)
    )
