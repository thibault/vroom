import math


class Motion:
    """Motion representation class."""

    def __init__(self, angle, speed):
        "angle in radius, speed in meter / second."""
        self.angle = angle
        self.speed = speed


class Coordinates:
    """Represents coordinates on the map."""
    def __init__(self, x_and_y, y=None):
        if isinstance(x_and_y, tuple):
            self.x, self.y = x_and_y
        else:
            self.x = x_and_y
            self.y = y

    def __repr__(self):
        return '<Coordinates(%s, %s)>' % (self.x, self.y)

    def distance(self, coord):
        y_dist = coord.y - self.y
        x_dist = coord.x - self.x
        dist = math.sqrt((y_dist ** 2) + (x_dist ** 2))
        return dist


def integrate(coord, motion, time):
    """Performs the position integration.

    See http://gafferongames.com/game-physics/integration-basics/

    TODO: replace the Euler integation with RK4.

    Time is given in milliseconds.
    """
    assert isinstance(coord, Coordinates)
    assert isinstance(motion, Motion)

    angle = motion.angle
    speed = motion.speed / 1000.0 * time
    new_x = coord.x + math.sin(angle) * speed
    new_y = coord.y + math.cos(angle) * speed

    return Coordinates(new_x, new_y)
