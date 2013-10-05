from physics import Coordinates


class Node:
    def __init__(self, coord):
        assert isinstance(coord, Coordinates)

        self.coord = coord

    def __repr__(self):
        return '<Node %s>' % self.coord


class Arc:
    def __init__(self, src, dest):
        assert isinstance(src, Coordinates)
        assert isinstance(dest, Coordinates)

        self.src = src
        self.dest = dest


class Road:
    """A road is just a graph. That's it."""
    arcs = list()

    def build(self, coords):
        assert len(coords) > 1

        src = Node(coords.pop())
        for coord in coords:
            dest = Node(coord)
            self.arcs.append(Arc(src, dest))
            src = dest
