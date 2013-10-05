import unittest

from physics import Coordinates
from roads import Road
from graphics import Graphic


class GraphicTests(unittest.TestCase):

    def setUp(self):
        self.coords = (
            Coordinates(100, 100),
            Coordinates(100, 300),
            Coordinates(500, 800),
        )
