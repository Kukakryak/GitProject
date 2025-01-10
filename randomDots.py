import pygame
import random
from time import sleep
pygame.init()

width = 1920
height = 1080
screen = pygame.display.set_mode([width,height])
running = True
screen.fill((255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i in range(0, 500):
            rwidth = random.randint(0, width)
            rheight = random.randint(0, height)
            pygame.draw.circle(screen, (0, 0, 255), (rwidth, rheight), 10)
            sleep(0.01)
            pygame.display.flip()


