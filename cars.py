import pygame

from physics import integrate


class Car:
    color = (255, 255, 255)

    def __init__(self, coord, motion):
        self.coordinates = coord
        self.motion = motion
        self.width = 3

    def __repr__(self):
        return '<Car (%s, %s)>' % (self.coordinates.x, self.coordinates.y)

    def update(self, delta):
        self.coordinates = integrate(self.coordinates, self.motion, delta)

    def draw(self, surface):
        rect = pygame.Rect(self.coordinates.x, self.coordinates.y,
                           self.width, self.width)
        pygame.draw.rect(surface, self.color, rect, 0)
