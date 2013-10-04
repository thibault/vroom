import datetime
import math
import pygame


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

    def __repr__(self):
        return '<Coordinates(%s, %s)>' % (self.x, self.y)

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

    def distance(self, coord):
        y_dist = coord.y - self.y
        x_dist = coord.x - self.x
        dist = math.sqrt((y_dist ** 2) + (x_dist ** 2))
        return dist


class Universe:
    def __init__(self):
        self.cars = list()
        self.nests = (
            Nest(Coordinates(100, 100),
                 Motion(math.pi / 2, 8.0),
                 frequency=5000),
        )

    def update(self, delta):
        """Update the universe status."""
        for nest in self.nests:
            new_cars = nest.generate_car(self.cars)
            if new_cars:
                self.cars.append(new_cars)

        for car in self.cars:
            car.update(delta)

    def draw(self, surface):
        for car in self.cars:
            car.draw(surface)


class Nest:
    """A nest is a car generator."""

    birth_frequency = 5 * 500
    max_cars = 5

    def __init__(self, coord, motion, frequency):
        assert isinstance(coord, Coordinates)
        self.coord = coord

        assert isinstance(motion, Motion)
        self.motion = motion

        self.frequency = frequency
        self.last_car_generated_at = datetime.datetime.now()

    def generate_car(self, cars):
        """Add new cars on the map if necessary."""
        now = datetime.datetime.now()
        last_generation_delta = now - self.last_car_generated_at
        milliseconds_delta = sum((last_generation_delta.seconds * 1000,
                                 last_generation_delta.microseconds / 1000))

        new_car = None
        if milliseconds_delta > self.birth_frequency and len(cars) < self.max_cars:
            new_car = Car(self.coord, self.motion)
            self.last_car_generated_at = now

        return new_car


class Car:
    def __init__(self, coord, motion):
        self.coordinates = coord
        self.motion = motion
        self.width = 3

    def __repr__(self):
        return '<Car (%s, %s)>' % (self.coordinates.x, self.coordinates.y)

    def update(self, delta):
        self.coordinates = self.coordinates.move(self.motion, delta)

    def draw(self, surface):
        rect = pygame.Rect(self.coordinates.x, self.coordinates.y,
                           self.width, self.width)
        pygame.draw.rect(surface, white, rect, 0)
