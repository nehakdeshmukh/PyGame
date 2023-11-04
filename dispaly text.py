# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 19:03:07 2023

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


# assigning values to X and Y variable
X = 800
Y = 800

# define our game's display and  resolution
gameDisplay = pygame.display.set_mode((X,Y))

# filling display with colour black
gameDisplay.fill(black)


# set the pygame window name
pygame.display.set_caption('Show Text')


sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

# create a font object.
# font file size of the font
font = pygame.font.Font(sysfont, 15)



# create a text surface object,
# on which text is drawn on it.
text = font.render('(0,0)', True, green)


# create a rectangular object for the
# text surface object
textRect = text.get_rect()


# set the center of the rectangular object.
# textRect.center = (X // 2, Y // 2)

# main application loop
run = True
while run:
    clock.tick(60)

    gameDisplay.blit(text, textRect)    

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update the display
    pygame.display.update()

pygame.quit()
exit()
