import sys
import pygame
import math

from world import Universe


# Initialize pygame
pygame.init()
size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
clock.tick(30)

# Initialize the universe
universe = Universe()
universe.add_nest(100, 100, math.pi / 2, 30.0)
universe.add_hole(600, 100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    universe.update(clock.get_time())
    universe.draw(screen)

    pygame.display.flip()
    clock.tick(30)
