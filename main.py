import pygame
import math
from pygame.locals import *
from settings import *
from player import *
from map import *

pygame.init()
clock = pygame.time.Clock()
screen = sc
running = True
player = Player()

surf = pygame.Surface((WIDTH, HALF_HEIGHT))
surf.fill(BLUE)
surf2 = pygame.Surface((100, 100))
surf2.fill(BLACK)

while running:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False

    controls = pygame.key.get_pressed()
    # if controls[pygame.K_a]:
    #             screen.blit(surf2, (x_pos2, y_pos2))
    #             x_pos2 += -5
    # if controls[pygame.K_s]:
    #             screen.blit(surf2, (x_pos2, y_pos2))
    #             y_pos2 += 5       
    # if controls[pygame.K_w]:
    #             screen.blit(surf2, (x_pos2, y_pos2))
    #             y_pos2 += -5
    # if controls[pygame.K_d]:
    #             screen.blit(surf2, (x_pos2, y_pos2))
    #             x_pos2 += 5

    if controls[pygame.K_KP_4]:
        player.move_left()
    if controls[pygame.K_KP_6]:
        player.move_right()
    if controls[pygame.K_KP_8]:
        player.move_forw()
    if controls[pygame.K_KP_5]:
        player.move_back()
    if controls[pygame.K_KP_7]:
        player.rotate(k if controls[pygame.K_KP_5] else -k)
    if controls[pygame.K_KP_9]:
        player.rotate(-k if controls[pygame.K_KP_5] else k)
        
    sc.fill(BLACK)
    sc.blit(surf, (0, 0)) 
    player.fov()
    # player.obj_1()
    for x, y in map:
        pygame.draw.rect(screen, GRAY, (x, y, x_size2, y_size2), 2)
    for x, y in G:
        pygame.draw.rect(screen, GRAY, (x, y, x_size3, x_size3), 2)
    player.draw()         
    pygame.display.flip() 
    clock.tick(FPS)
    
pygame.quit()

# import pygame
# from pygame.locals import *
# from settings import *
# from player import *

# pygame.init()
# clock = pygame.time.Clock()
# screen = sc
# running = True

# player = Player()

# surf = pygame.Surface((100, 100))
# surf.fill(LIGHT_GREEN)
# surf2 = pygame.Surface((100, 100))
# surf2.fill(BLACK)

# while running:
#     for event in pygame.event.get():
         
#         if event.type == pygame.QUIT:
#             running = False
#         controls = pygame.key.get_pressed()
#         if controls[pygame.K_a]:
#                     screen.blit(surf2, (x1, y1))
#                     x1 += -5
#         if controls[pygame.K_s]:
#                     screen.blit(surf2, (x1, y1))
#                     y1 += 5       
#         if controls[pygame.K_w]:
#                     screen.blit(surf2, (x1, y1))
#                     y1 += -5
#         if controls[pygame.K_d]:
#                     screen.blit(surf2, (x1, y1))
#                     x1 += 5

#         if controls[pygame.K_LEFT]:
#             player.move(x = -1)
#         if controls[pygame.K_RIGHT]:
#             player.move(x = 1)
#         if controls[pygame.K_UP]:
#             player.move(y = -1)
#         if controls[pygame.K_DOWN]:
#             player.move(y = 1)
        
#     screen.fill(BLACK)
#     screen.blit(surf, (x1, y1))
#     player.draw()           
#     pygame.display.flip() 
#     clock.tick(60)
    
# pygame.quit()