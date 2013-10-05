import math
import random

from physics import Coordinates


class Car:
    def __init__(self, arc, speed):
        self.arc = arc
        self.distance = 0
        self.speed = speed
        self.desired_speed = random.randint(30, 60)
        self.acceleration = 6.67

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
        current_accel = 0.0
        if self.speed < self.desired_speed:
            self.speed += self.acceleration * delta / 1000.0
            current_accel = self.acceleration

        # http://fr.wikipedia.org/wiki/Acc%C3%A9l%C3%A9ration#Calcul_de_la_distance_parcourue
        self.distance += (current_accel * delta * delta / 2000000.0) + self.speed * delta / 1000.0
