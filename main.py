import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEUROFROG")

# load images
frog_img = pygame.image.load("img/")

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()

road = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

