# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:56:31 2023

@author: nehak
"""

import pygame

pygame.init()

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

# 400 300
pygame.draw.line(gameDisplay, red, (0, 300), (800, 300), 1)
pygame.draw.line(gameDisplay, green, (400, 0), (400, 600), 1)


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