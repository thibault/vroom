import unittest

from physics import Coordinates
from roads import Road


class RoadTests(unittest.TestCase):
    def setUp(self):
        self.coords = (
            Coordinates(100, 100),
            Coordinates(100, 300),
            Coordinates(500, 800),
        )

    def test_build(self):
        road = Road()
        road.build(self.coords)

        self.assertEqual(len(road.arcs), 2)
