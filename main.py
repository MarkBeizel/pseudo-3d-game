import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()