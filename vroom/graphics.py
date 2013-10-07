import pygame


class Graphic:
    car_color = (255, 50, 50)
    car_width = 3
    road_color = (255, 255, 255)
    road_width = 6
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
        acceleration_rate = car.acceleration_rate
        rect = pygame.Rect(coord.x, coord.y,
                           self.car_width, self.car_width)

        # Change car color depending on acceleration
        if acceleration_rate > 0:
            color = (0, 0, 255)
        else:
            color = (255, 0, 0)
        pygame.draw.rect(self.surface, color, rect, 0)

    def draw_road(self, road):
        pointlist = road.pointlist()
        closed = False
        pygame.draw.lines(self.surface, self.road_color, closed, pointlist,
                          self.road_width)
