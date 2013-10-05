import math


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
