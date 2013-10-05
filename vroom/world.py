from graphics import Graphic


class Universe:
    def __init__(self, surface):
        self.roads = list()
        self.graphic = Graphic(surface)

    def add_road(self, road):
        self.roads.append(road)

    def update(self, delta):
        """Update the universe status."""
        for road in self.roads:
            road.update(delta)

    def draw(self):
        for road in self.roads:
            self.graphic.draw(road)
            for car in road.cars:
                self.graphic.draw(car)
