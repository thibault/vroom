import sys
import pygame

from world import Universe


# Initialize pygame
pygame.init()
size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Initialize the universe
universe = Universe()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    universe.update(clock.get_time())
    universe.draw(screen)

    pygame.display.flip()
    clock.tick(30)
