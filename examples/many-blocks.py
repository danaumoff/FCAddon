import pygame
import random
from block import Block

RESOLUTION = (800, 600)
BLACK = (0, 0, 0)
FPS = 120
running = True

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("DVD")
clock = pygame.time.Clock()

blocks = []
for i in range(2):
    blocks.append(Block(screen, random.randint(100, 200), random.randint(50, 150), random.randint(10, 595), random.randint(10, 440)))
    a = True
    while a:
        a = False
        for param in range(len(blocks)-1):
            if blocks[param].block_collision(blocks[-1]):
                blocks.pop()
                a = True
                blocks.append(Block(screen, random.randint(100, 200), random.randint(50, 150), random.randint(10, 595), random.randint(10, 440)))
    blocks[-1].speed(random.randint(-15, 15) / 10, random.randint(-15, 15) / 10)
    blocks[-1].gravity(0, 0)
    blocks[-1].color_change()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    for i in range(len(blocks)):
        blocks[i].update()
        blocks[i].wall_collision()
        for j in range(len(blocks)):
            if i != j:
                blocks[i].block_collision(blocks[j])



    pygame.display.flip()

pygame.quit()