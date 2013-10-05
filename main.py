import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'vroom'))

import pygame

from world import Universe
from roads import Road


# Initialize pygame
pygame.init()
size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
clock.tick(30)

# Initialize the universe
universe = Universe(screen)

road_coords = (
    (100, 100),
    (150, 300),
    (250, 500),
    (400, 500),
    (700, 200))
road = Road(road_coords)
universe.add_road(road)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    universe.update(clock.get_time())
    universe.draw()

    pygame.display.flip()
    clock.tick(30)
