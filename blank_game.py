import pygame
import sys
import os
from pygame.locals import *
import math
pygame.init()


DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption('Doggie!')
FPS= 60
fpsClock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
sky_blue = (0, 180, 230)
yellow = (255, 255, 0)
green = (0, 255, 0)

#Scenery
def scenery():
    DISPLAYSURF.fill(sky_blue)
    sun = pygame.draw.circle(DISPLAYSURF, yellow, (400, 50), 30, 0)
    landscape = pygame.draw.rect(DISPLAYSURF, green, (0, 350, 500, 400))


dogImg1 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (1).png')
dogImg1 = pygame.transform.scale(dogImg1, (60, 80))
dogImg2 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (2).png')
dogImg2 = pygame.transform.scale(dogImg2, (60, 80))
dogImg3 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (3).png')
dogImg3 = pygame.transform.scale(dogImg3, (60, 80))
dogImg4 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (4).png')
dogImg4 = pygame.transform.scale(dogImg4, (60, 80))
dogImg5 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (5).png')
dogImg5 = pygame.transform.scale(dogImg5, (60, 80)) 
dogImg6 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (6).png')
dogImg6 = pygame.transform.scale(dogImg6, (60, 80))

while True:
    scenery()
    for i in range(600):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        a = 0
        DISPLAYSURF.blit(dogImg1, (a+i,280))
        pygame.display.flip()
        pygame.display.update()
        a = a+1
        scenery()
        DISPLAYSURF.blit(dogImg2, (a + i, 280))
        pygame.display.flip()
        pygame.display.update()
        a = a+1
        scenery()
        DISPLAYSURF.blit(dogImg3, (a + i, 280))
        scenery()
        pygame.display.flip()
        pygame.display.update()
        a = a+1
        scenery()
        DISPLAYSURF.blit(dogImg4, (a + i, 280))
        pygame.display.flip()
        pygame.display.update()
        a = a+1
        scenery()
        DISPLAYSURF.blit(dogImg5, (a + i, 280))
        pygame.display.flip()
        pygame.display.update()
        a = a+1
        scenery()
        DISPLAYSURF.blit(dogImg6, (a + i, 280))
        pygame.display.flip()
        fpsClock.tick(FPS)
        a = a+3


    pygame.display.update()
    fpsClock.tick(FPS)

