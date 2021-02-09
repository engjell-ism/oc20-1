import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

w, h = 500, 500
angle = 0
scale = 1
pygame.init()
screen = pygame.display.set_mode(path)

img0 = pygame.image.load(path)
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
            
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            
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
            
        rect = img.get_rect()
        rect.center = center
                

    screen.fill(GRAY)
    pygame.draw.rect(img0, GREEN, rect0, 1)
    screen.blit(img, rect)
    pygame.display.flip()

pygame.quit()