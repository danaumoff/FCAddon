import pygame
import random
import math
from circle import Circle

RES = (800, 600)
BLACK = (0, 0, 0)
FPS = 120
running = True

pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("DVD")
clock = pygame.time.Clock()

circle = Circle(screen, 10)
pygame.draw.circle().co
circle.color_change()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    # screen.fill(BLACK)
    circle.update()





    pygame.display.flip()

pygame.quit()
