from physics import Coordinates


class Node:
    def __init__(self, coord):
        assert isinstance(coord, Coordinates)

        self.coord = coord

    def __repr__(self):
        return '<Node %s>' % self.coord


class Arc:
    def __init__(self, src, dest):
        assert isinstance(src, Node)
        assert isinstance(dest, Node)

        self.src = src
        self.dest = dest


class Road:
    """A road is just a graph. That's it."""

    def __init__(self):
        self.arcs = list()

    def build(self, coords):
        assert len(coords) > 1

        if not isinstance(coords, list):
            coords = list(coords)

        src = Node(coords.pop())
        for coord in coords:
            dest = Node(coord)
            self.arcs.append(Arc(src, dest))
            src = dest
