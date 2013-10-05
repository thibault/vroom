import datetime
import math

from physics import Coordinates, Motion
from cars import Car


class Node(object):
    """This is a node in a road."""
    def __init__(self, coord):
        assert isinstance(coord, Coordinates)

        self.coord = coord

    def __repr__(self):
        return '<Node %s>' % self.coord


class Nest(Node):
    """A nest is a special node that generates cars."""

    def __init__(self, coord, max_cars, birth_frequency):
        super(Nest, self).__init__(coord)
        self.max_cars = max_cars
        self.birth_frequency = birth_frequency
        self.last_car_generated_at = datetime.datetime(1970, 1, 1)

    def __repr__(self):
        return '<Nest %s>' % self.coord

    def generate_cars(self, nb_cars):
        """Add new cars on the map if necessary."""
        now = datetime.datetime.now()
        last_generation_delta = now - self.last_car_generated_at
        milliseconds_delta = sum((last_generation_delta.seconds * 1000,
                                 last_generation_delta.microseconds / 1000))

        new_car = None
        if milliseconds_delta > self.birth_frequency and nb_cars < self.max_cars:
            new_car = Car(self.coord, Motion(math.pi / 2, 30))
            self.last_car_generated_at = now

        return new_car


class Hole(Node):
    """A special node that deletes cars that crosses it."""
    radius = 20

    def __init__(self, coord):
        assert isinstance(coord, Coordinates)
        self.coord = coord

    def __repr__(self):
        return '<Hole %s>' % self.coord

    def filter(self, car):
        return car.coordinates.distance(self.coord) > self.radius


class Arc:
    def __init__(self, src, dest):
        assert isinstance(src, Node)
        assert isinstance(dest, Node)

        self.src = src
        self.dest = dest

    def __repr__(self):
        return '<Arc (%s,%s)->(%s,%s)>' % (self.src.coord.x, self.src.coord.y,
                                           self.dest.coord.x, self.dest.coord.y)

    @property
    def angle(self):
        """Get the angle of the current arc."""
        x = self.dest.coord.x - self.src.coord.x
        y = self.dest.coord.y - self.src.coord.y
        angle = math.atan(y / x)
        return angle


class Road:
    """A road is just a graph. That's it."""

    def __init__(self, coords, max_cars=20, frequency=200):
        self.nest = None
        self.hole = None
        self.cars = list()
        self.arcs = list()

        assert len(coords) > 1

        src = Nest(Coordinates(coords[0]), max_cars, frequency)
        self.nest = src
        for coord in coords[1:-1]:
            dest = Node(Coordinates(coord))
            self.arcs.append(Arc(src, dest))
            src = dest
        dest = Hole(Coordinates(coords[-1]))
        self.hole = dest
        self.arcs.append(Arc(src, dest))

        self.cars = (
            Car(self.arcs[0], 30),
        )

    def pointlist(self):
        """Returns a list of tuples corresponding to the nodes coordinates."""
        points = list()
        for arc in self.arcs:
            points.append((arc.src.coord.x, arc.src.coord.y))
        points.append((arc.dest.coord.x, arc.dest.coord.y))

        return points

    def update(self, delta):
        """Update the road status."""
        #new_cars = self.nest.generate_cars(len(self.cars))
        #if new_cars:
        #    self.cars.append(new_cars)

        self.cars = filter(self.hole.filter, self.cars)

        for car in self.cars:
            car.update(delta)
