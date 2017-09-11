import pygame
import sys
import os
from pygame.locals import *
pygame.init()


DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption('Doggie!')
FPS= 30
fpsClock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
sky_blue = (0, 180, 230)
yellow = (255, 255, 0)
green = (0, 255, 0)

#Scenery
#while True:
DISPLAYSURF.fill(sky_blue)
sun = pygame.draw.circle(DISPLAYSURF, yellow, (400, 50), 30, 0)
landscape = pygame.draw.rect(DISPLAYSURF, green, (0, 350, 500, 400))
dogImg = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (6).png')
dogImg = pygame.transform.scale(dogImg, (60, 80))
DISPLAYSURF.blit(dogImg,(0,280))
pygame.display.flip()
#c.tick(3)


#dogx = 10
#dogy = 10
#direction = 'right'

#continuous running loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
