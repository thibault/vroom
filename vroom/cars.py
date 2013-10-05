import math

from physics import Coordinates


class Car:
    def __init__(self, arc, speed):
        self.arc = arc
        self.distance = 0
        self.speed = speed

    def __repr__(self):
        return '<Car (%s, %s)>' % (self.coordinates.x, self.coordinates.y)

    def set_arc(self, arc):
        self.arc = arc
        self.distance = 0

    @property
    def coordinates(self):
        """Get absolute coordinates of the car.

        Coordinates depends on the arc initial node.

        """
        angle = self.arc.angle
        coord = self.arc.src.coord

        dx = math.cos(angle) * self.distance
        x = coord.x + dx

        dy = math.sin(angle) * self.distance
        y = coord.y + dy

        return Coordinates(x, y)

    def update(self, delta):
        self.distance += self.speed / 1000.0 * delta
