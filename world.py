import pygame
import math


white = (255, 255, 255)


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
        self.coordinates = (x, y)
        self.motion = (angle, speed)

    def update(self, delta):
        self.coordinates = self.integrate(self.coordinates, self.motion, delta)

    def integrate(self, coordinates, motion, delta):
        speed = motion[1] / 1000.0 * delta
        new_x = coordinates[0] + math.sin(motion[0]) * speed
        new_y = coordinates[1] + math.cos(motion[0]) * speed
        return (new_x, new_y)

    def draw(self, surface):
        rect = pygame.Rect(int(self.coordinates[0]), int(self.coordinates[1]), 3, 3)
        pygame.draw.rect(surface, white, rect, 0)
