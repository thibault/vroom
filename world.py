import pygame


white = (255, 255, 255)


class Universe:
    def __init__(self):
        self.cars = (
            Car(100, 100, 90, 30),
        )

    def update(self, delta):
        """Update the universe status."""
        for car in self.cars:
            car.update(delta)

    def draw(self, surface):
        for car in self.cars:
            car.draw(surface)


class Car:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed

    def update(self, delta):
        pass

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, 3, 3)
        pygame.draw.rect(surface, white, rect, 0)
