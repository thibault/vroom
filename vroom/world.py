import datetime

from physics import Motion, Coordinates
from roads import Road
from cars import Car
from graphics import Graphic


class Universe:
    def __init__(self, surface):
        self.roads = list()
        self.cars = list()
        self.nests = list()
        self.holes = list()
        self.graphic = Graphic(surface)

    def add_nest(self, x, y, angle, speed, frequency=5000):
        self.nests.append(Nest(Coordinates(x, y),
                               Motion(angle, speed),
                               frequency))

    def add_hole(self, x, y):
        self.holes.append(Hole(Coordinates(x, y)))

    def add_road(self, coords):
        road = Road()
        coords = [Coordinates(coord[0], coord[1]) for coord in coords]
        road.build(coords)
        self.roads.append(road)

    def update(self, delta):
        """Update the universe status."""
        for nest in self.nests:
            new_cars = nest.generate_car(self.cars)
            if new_cars:
                self.cars.append(new_cars)

        for hole in self.holes:
            self.cars = filter(hole.filter, self.cars)

        for car in self.cars:
            car.update(delta)

    def draw(self):
        for road in self.roads:
            self.graphic.draw(road)

        for car in self.cars:
            self.graphic.draw(car)


class Nest:
    """Generates new car."""

    birth_frequency = 5 * 500
    max_cars = 5

    def __init__(self, coord, motion, frequency):
        assert isinstance(coord, Coordinates)
        self.coord = coord

        assert isinstance(motion, Motion)
        self.motion = motion

        self.frequency = frequency
        self.last_car_generated_at = datetime.datetime(1970, 1, 1)

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


class Hole:
    """Special objects that deletes cars coming too close."""
    radius = 20

    def __init__(self, coord):
        assert isinstance(coord, Coordinates)
        self.coord = coord

    def filter(self, car):
        return car.coordinates.distance(self.coord) > self.radius
