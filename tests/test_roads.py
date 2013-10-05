import unittest

from roads import Road


class RoadTests(unittest.TestCase):
    def setUp(self):
        self.coords = (
            (100, 100),
            (100, 300),
            (500, 800),
        )

    def test_build(self):
        road = Road(self.coords)

        self.assertEqual(len(road.arcs), 2)

    def test_pointlist(self):
        road = Road(self.coords)

        self.assertEqual(road.pointlist(), [
            (100, 100),
            (100, 300),
            (500, 800),
        ])
