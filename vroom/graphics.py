import pygame


class Graphic:
    car_color = (255, 50, 50)
    road_color = (50, 255, 50)
    draw_methods = {
        'Car': 'draw_car',
        'Road': 'draw_road',
    }

    def __init__(self, surface):
        self.surface = surface

    def draw(self, obj):
        object_class = obj.__class__.__name__
        method_name = self.draw_methods.get(object_class, None)
        if method_name:
            method = getattr(self, method_name)
            method(obj)

    def draw_car(self, car):
        coord = car.coordinates
        rect = pygame.Rect(coord.x, coord.y,
                           car.width, car.width)
        pygame.draw.rect(self.surface, self.car_color, rect, 0)

    def draw_road(self, road):
        pointlist = road.pointlist()
        closed = False
        pygame.draw.lines(self.surface, self.road_color, closed, pointlist, 5)
