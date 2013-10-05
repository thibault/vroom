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

    def __repr__(self):
        return '<Arc (%s,%s)->(%s,%s)>' % (self.src.coord.x, self.src.coord.y,
                                           self.dest.coord.x, self.dest.coord.y)


class Road:
    """A road is just a graph. That's it."""

    def __init__(self):
        self.arcs = list()

    def build(self, coords):
        """Build a road from coordinates."""
        assert len(coords) > 1

        if not isinstance(coords, list):
            coords = list(coords)

        src = None
        for coord in coords:
            dest = Node(coord)
            if src:
                self.arcs.append(Arc(src, dest))
            src = dest

    def pointlist(self):
        """Returns a list of tuples corresponding to the nodes coordinates."""
        points = list()
        for arc in self.arcs:
            points.append((arc.src.coord.x, arc.src.coord.y))
        points.append((arc.dest.coord.x, arc.dest.coord.y))

        return points
