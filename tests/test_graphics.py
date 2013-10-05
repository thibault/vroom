import unittest

from physics import Coordinates


class GraphicTests(unittest.TestCase):

    def setUp(self):
        self.coords = (
            (100, 100),
            (100, 300),
            (500, 800),
        )
