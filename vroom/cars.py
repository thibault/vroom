import math
import random

from physics import Coordinates


class IDM:
    """Intelligent Driver Model implementation.

    See http://en.wikipedia.org/wiki/Intelligent_Driver_Model

    """
    accel_exponent = 4

    def __init__(self):
        self.desired_velocity = random.uniform(25, 36)  # 90 ~ 130 km/h
        self.minimum_gap = random.uniform(1.5, 3)
        self.safe_time_headway = random.uniform(0.8, 2)
        self.maximum_acceleration = random.uniform(1, 3)
        self.desired_deceleration = random.uniform(2, 3)

    def step(self, time_delta,
             speed, acceleration,
             leading_car_distance,
             approaching_rate):

        new_speed = speed + acceleration * time_delta / 1000.0

        accel_component = (speed / self.desired_velocity) ** self.accel_exponent
        # TODO : make this look less ugly
        decel_component = ((self.minimum_gap + speed * self.safe_time_headway + (speed * approaching_rate / (2 * math.sqrt(self.maximum_acceleration * self.desired_deceleration)))) / leading_car_distance) ** 2
        accel = self.maximum_acceleration * (1 - accel_component - decel_component)

        return {
            'speed': new_speed,
            'acceleration': accel,
        }


class Car:
    def __init__(self, arc, speed, distance=0):
        self.arc = arc
        self.distance = distance
        self.speed = speed
        self.acceleration = 0

        self.driver_model = IDM()

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

    @property
    def acceleration_rate(self):
        """Returns rate between current acceleration and max acceleration."""
        if self.acceleration >= 0:
            rate = self.acceleration / self.driver_model.maximum_acceleration
        else:
            rate = self.acceleration / self.driver_model.desired_deceleration

        return rate

    def update(self, universe, delta):
        """Integrate the new car position."""
        leading_car = universe.leading_car(self)
        leading_distance = leading_car.coordinates.distance(self.coordinates)
        approaching_rate = self.speed - leading_car.speed

        step = self.driver_model.step(delta, self.speed, self.acceleration,
                                      leading_distance, approaching_rate)
        self.speed = step['speed']
        self.acceleration = step['acceleration']

        # http://fr.wikipedia.org/wiki/Acc%C3%A9l%C3%A9ration#Calcul_de_la_distance_parcourue
        self.distance += (self.acceleration * delta * delta / 2000000.0) + self.speed * delta / 1000.0
