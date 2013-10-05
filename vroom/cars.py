import math
import random

from physics import Coordinates


class Car:
    def __init__(self, arc, speed, distance=0):
        self.arc = arc
        self.distance = distance
        self.speed = speed
        self.desired_speed = random.randint(30, 60)
        self.acceleration = 6.67
        self.desired_front_distance = random.randint(5, 15)

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

    def update(self, universe, delta):
        """Integrate the new car position.

        If there are cars in front of us, brake.
        Otherwise, if we go too slow, accelerate.

        """
        current_accel = 0.0

        front_car_distance = universe.next_car_distance(self)
        if front_car_distance < self.desired_front_distance:
            self.speed -= self.acceleration * 3 * delta / 1000.0
            self.speed = max(self.speed, 0)
        elif self.speed < self.desired_speed:
            self.speed += self.acceleration * delta / 1000.0
            current_accel = self.acceleration

        # http://fr.wikipedia.org/wiki/Acc%C3%A9l%C3%A9ration#Calcul_de_la_distance_parcourue
        self.distance += (current_accel * delta * delta / 2000000.0) + self.speed * delta / 1000.0
