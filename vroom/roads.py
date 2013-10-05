import datetime
import math

from physics import Coordinates
from cars import Car


class Node(object):
    """This is a node in a road."""
    def __init__(self, coord):
        assert isinstance(coord, Coordinates)

        self.coord = coord

    def __repr__(self):
        return '<Node %s>' % self.coord


class Hole(Node):
    """A special node that deletes cars that crosses it."""
    radius = 20

    def __repr__(self):
        return '<Hole %s>' % self.coord

    def filter(self, car):
        return car.coordinates.distance(self.coord) > self.radius


class Arc:
    def __init__(self, src, dest, index):
        assert isinstance(src, Node)
        assert isinstance(dest, Node)

        self.src = src
        self.dest = dest
        self.index = index

    def __repr__(self):
        return '<Arc (%s,%s)->(%s,%s)>' % (self.src.coord.x, self.src.coord.y,
                                           self.dest.coord.x, self.dest.coord.y)

    @property
    def angle(self):
        """Get the angle of the current arc."""
        dx = float(self.dest.coord.x - self.src.coord.x)
        dy = float(self.dest.coord.y - self.src.coord.y)
        angle = math.atan(dy / dx)

        if dx < 0 and dy < 0:
            angle = angle - math.pi
        elif dx < 0 and dy > 0:
            angle = angle + math.pi
        return angle

    @property
    def length(self):
        return self.src.coord.distance(self.dest.coord)


class Road:
    """A road is just a graph. That's it."""

    def __init__(self, coords, max_cars=20, birth_frequency=500):
        self.hole = None
        self.cars = list()
        self.arcs = list()
        self.max_cars = max_cars
        self.birth_frequency = birth_frequency
        self.last_car_generated_at = datetime.datetime(1970, 1, 1)

        assert len(coords) > 1

        src = None
        arc_index = 0
        for coord in coords[0:-1]:
            dest = Node(Coordinates(coord))
            if src:
                self.arcs.append(Arc(src, dest, arc_index))
                arc_index += 1
            src = dest

        dest = Hole(Coordinates(coords[-1]))
        self.hole = dest
        self.arcs.append(Arc(src, dest, arc_index))

    def generate_cars(self, nb_cars):
        """Add new cars on the map if necessary."""
        now = datetime.datetime.now()
        last_generation_delta = now - self.last_car_generated_at
        milliseconds_delta = sum((last_generation_delta.seconds * 1000,
                                 last_generation_delta.microseconds / 1000))

        new_car = None
        if milliseconds_delta > self.birth_frequency and nb_cars < self.max_cars:
            new_car = Car(self.arcs[0], 100)
            self.last_car_generated_at = now

        return new_car

    def pointlist(self):
        """Returns a list of tuples corresponding to the nodes coordinates."""
        points = list()
        for arc in self.arcs:
            points.append((arc.src.coord.x, arc.src.coord.y))
        points.append((arc.dest.coord.x, arc.dest.coord.y))

        return points

    def update(self, delta):
        """Update the road status."""
        new_cars = self.generate_cars(len(self.cars))
        if new_cars:
            self.cars.append(new_cars)

        self.cars = filter(self.hole.filter, self.cars)

        for car in self.cars:
            car.update(delta)
            if car.distance >= car.arc.length:
                arc = self.arcs[car.arc.index + 1]
                car.set_arc(arc)
