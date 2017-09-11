import pygame
import sys
import os
from pygame.locals import *
import math
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
def scenery():
    DISPLAYSURF.fill(sky_blue)
    sun = pygame.draw.circle(DISPLAYSURF, yellow, (400, 50), 30, 0)
    landscape = pygame.draw.rect(DISPLAYSURF, green, (0, 350, 500, 400)) 
    
while True:
    scenery()
    for i in range(400):
        DISPLAYSURF.fill(sky_blue)
        sun = pygame.draw.circle(DISPLAYSURF, yellow, (400, 50), 30, 0)
        landscape = pygame.draw.rect(DISPLAYSURF, green, (0, 350, 500, 400))
        dogImg1 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (1).png')
        dogImg2 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (2).png') 
        dogImg3 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (3).png')
        dogImg4 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (4).png')
        dogImg5 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (5).png')
        dogImg6 = pygame.image.load('C:/Users/Mygan/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/catndog/png/dog/Run (6).png')
        dogImg = pygame.transform.scale(dogImg1, (60, 80))
        a = 5
        DISPLAYSURF.blit(dogImg, (a + i,280))
        pygame.display.flip()
        a = a+5
        dogImg = pygame.transform.scale(dogImg2, (60, 80))
        scenery()
        DISPLAYSURF.blit(dogImg, (a + i, 280))
        pygame.display.flip()
        a = a+5
        dogImg = pygame.transform.scale(dogImg3, (60, 80))
        scenery()
        DISPLAYSURF.blit(dogImg, (a + i, 280))
        scenery()
        pygame.display.flip()
        a = a+5
        dogImg = pygame.transform.scale(dogImg4, (60, 80))
        scenery()
        DISPLAYSURF.blit(dogImg, (a + i, 280))
        pygame.display.flip()
        a = a+5
        dogImg = pygame.transform.scale(dogImg5, (60, 80))
        scenery()
        DISPLAYSURF.blit(dogImg, (a + i, 280))
        pygame.display.flip()
        a = a+5
        dogImg = pygame.transform.scale(dogImg6, (60, 80))
        scenery()
        DISPLAYSURF.blit(dogImg, (a + i, 280))
        pygame.display.flip()
        a = a+5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
#dogx = 10
#dogy = 10
#direction = 'right'

#continuous running loop
#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    pygame.display.update()
#    fpsClock.tick(FPS)
