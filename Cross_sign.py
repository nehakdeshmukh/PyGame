# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:57:53 2023

@author: nehak
"""

import pygame

# initiate PyGame
pygame.init()

# to track time within the game
clock = pygame.time.Clock()

#colors
white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# define our game's display and  resolution
gameDisplay = pygame.display.set_mode((800,600))

# filling display with colour black
gameDisplay.fill(black)

#define pixel array
pixAr = pygame.PixelArray(gameDisplay)

for i in range(0,800):
    for j in range(0,600):
        pixAr[i][300] = red
        
        
# main application loop
run = True
while run:
    clock.tick(60)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update the display
    pygame.display.update()

pygame.quit()
exit()
