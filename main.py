import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEUROFROG")

# load images
car_img = pygame.image.load("img/car.png")
bg_img = pygame.image.load("img/bg.png")
frog_img = pygame.image.load("img/frog.png")
road_img = pygame.image.load("img/road.png")

run = True
while run:

  screen.blit(bg_img, (0, 0))
  screen.blit(frog_img, (448, 576))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

road = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

