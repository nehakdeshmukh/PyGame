# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:00:51 2023

@author: nehak
"""


import pygame

pygame.init()

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

X=300
Y=300

gamedisplay = pygame.display.set_mode((X,Y))

# gamedisplay.fill(black)

rect = pygame.Rect(0, 0, 20, 20)
rect.center = gamedisplay.get_rect().center
vel=5

# main application loop
run = True
while run:
    clock.tick(60)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            
            
    keys=pygame.key.get_pressed() 
        
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rect.centerx = rect.centerx % gamedisplay.get_width()
    rect.centery = rect.centery % gamedisplay.get_height()
    
    gamedisplay.fill(0)
    pygame.draw.rect(gamedisplay, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()