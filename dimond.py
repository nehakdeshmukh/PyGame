# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:47:32 2023

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
gameDisplay = pygame.display.set_mode((800,800))

# filling display with colour black
gameDisplay.fill(black)

#define pixel array
pixAr = pygame.PixelArray(gameDisplay)

for i in range(0,800):
    pixAr[i][i] = green
    pixAr[800-1-i][i] = green
    pixAr[i][400] = red
    pixAr[400][i] = red
    
for i in range(0,400):
        pixAr[400-1-i][i+1] = white
        pixAr[400+i][i+1] = white
        pixAr[i][400+i] = white
        

# pygame.draw.line(gameDisplay, white, (0, 400), (400, 0), 1)
# pygame.draw.line(gameDisplay, white, (0, 400), (400, 800), 1)
# pygame.draw.line(gameDisplay, white, (800, 400), (400, 0), 1)
# pygame.draw.line(gameDisplay, white, (800, 400), (400, 800), 1)

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
