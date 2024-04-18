import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEUROFROG")

# load images
car_img = pygame.image.load("img/car.png")
bg_img = pygame.image.load("img/bg.png")
frog_img = pygame.image.load("img/frog.png")
road_img = pygame.image.load("img/road.png")

# define program variables
TILE_SIZE = 48

def draw_grid():
  for line in range(0,24):
    pygame.draw.line(screen, (255, 255, 255), (0, line * TILE_SIZE), (SCREEN_WIDTH,line * TILE_SIZE))
    pygame.draw.line(screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, SCREEN_HEIGHT))

run = True
while run:

  screen.blit(bg_img, (0, 0))
  screen.blit(frog_img, (448, 576))

  draw_grid()


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

road = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

