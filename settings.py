# importing every thing needed to run the program
import pygame, random, math, sys, time

# setting up a font
pygame.init()
basicFont = pygame.font.SysFont(None, 20)

# setting up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 230)

# defining the screen size and the frames per second
WIDTH = 800
HEIGHT = 650
FPS = 30

# setting up some variables for the main program
thingProcess = False
draw = 0
running = True

# setting up sprite groups
allSprites = pygame.sprite.Group()
points = pygame.sprite.Group()
