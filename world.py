import pygame
import math


white = (255, 255, 255)


class Motion:
    """Motion representation class."""

    def __init__(self, angle, speed):
        "angle in radius, speed in meter / second."""
        self.angle = angle
        self.speed = speed


class Coordinates:
    """Represents coordinates on the map."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, motion, time):
        """Add given motion to coordinates.

        Time is given in milliseconds.

        """
        assert isinstance(motion, Motion)

        angle = motion.angle
        speed = motion.speed / 1000.0 * time
        new_x = self.x + math.sin(angle) * speed
        new_y = self.y + math.cos(angle) * speed

        return Coordinates(new_x, new_y)


class Universe:
    def __init__(self):
        self.cars = (
            Car(100.0, 100.0, math.pi / 2, 8.0),
        )

    def update(self, delta):
        """Update the universe status."""
        for car in self.cars:
            car.update(delta)

    def draw(self, surface):
        for car in self.cars:
            car.draw(surface)


class Car:
    def __init__(self, x, y, angle, speed):
        self.coordinates = Coordinates(x, y)
        self.motion = Motion(angle, speed)
        self.width = 3

    def update(self, delta):
        self.coordinates = self.coordinates.move(self.motion, delta)

    def draw(self, surface):
        rect = pygame.Rect(self.coordinates.x, self.coordinates.y,
                           self.width, self.width)
        pygame.draw.rect(surface, white, rect, 0)
