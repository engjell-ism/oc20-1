import pygame
from pygame.locals import *
import math, sys, os

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


w, h = 500, 500
angle = 0
scale = 1
pygame.init()
screen = pygame.display.set_mode((w, h))

mouse = pygame.mouse.get_pos()

img0 = pygame.image.load('bird.png')
img0.convert()

rect0 = img0.get_rect()
center = w//2, h//2
img = img0
rect = img.get_rect()
rect.center = center



moving = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
                
        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        #ici, on peut rajouter un "and moving" pour faire en sorte que l'image se transforme que lorsque l'on click sur la souris   
            
        elif event.type == MOUSEMOTION:
            rect.move_ip(event.rel)
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            d = math.sqrt(x ** 2 + y ** 2)
            angle = math.degrees(-math.atan2(y, x))
            scale = abs(5 * d / w)
            img = pygame.transform.rotozoom(img0, angle, scale)
            rect = img.get_rect()
            rect.center = center
            
        elif event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)
                
            elif event.key == K_s:
                if event.mod &KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
                
            elif event.key == K_o:
                img = img0
                angle = 0
                scale = 1
                
            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
                
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
                
            elif event.key == K_l:
                img = pygame.transform.laplacian(img)
                
            elif event.key == K_2:
                img = pygame.transform.scale2x(img)
                 

    screen.fill(GRAY)
    pygame.draw.rect(img0, GREEN, rect0, 1)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.draw.line(screen, GREEN, center, mouse, 1)
    pygame.draw.circle(screen, RED, center, 6, 1)
    pygame.draw.circle(screen, RED, mouse, 6, 1)
    pygame.display.flip()

pygame.quit()