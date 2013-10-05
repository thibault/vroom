import pygame

from cars import Car


class Graphic:
    color = (255, 255, 255)

    def __init__(self, surface):
        self.surface = surface

    def draw(self, obj):
        if isinstance(obj, Car):
            self.draw_car(obj)

    def draw_car(self, car):
        coord = car.coordinates
        rect = pygame.Rect(coord.x, coord.y,
                           car.width, car.width)
        pygame.draw.rect(self.surface, self.color, rect, 0)
