import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600), 0)
pygame.display.set_caption('Simple Pygame Game')
bee = pygame.image.load('bee1.png').convert_alpha()
beeX = 0
beeY = 0
clock = pygame.time.Clock()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT \
            or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    keystate = pygame.key.get_pressed()
    if keystate[K_RIGHT]:
        beeX += 5

    screen.fill((0,120,0))
    screen.blit(bee, (beeX, beeY))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()