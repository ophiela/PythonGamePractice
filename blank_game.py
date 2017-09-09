import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption('Hello World!')

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
sky_blue = (0, 200, 200)
yellow = (255, 255, 0)

#Scenery
DISPLAYSURF.fill(sky_blue)
pygame.draw.circle(DISPLAYSURF, yellow, (400, 50), 30, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
