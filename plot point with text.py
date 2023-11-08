# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:27:12 2023

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

X=800
Y=800

gamedisplay = pygame.display.set_mode((X,Y))

gamedisplay.fill(black)

sysfont = pygame.font.get_default_font()
print('system font : ', sysfont)

font = pygame.font.Font(sysfont, 15)

pixAr = pygame.PixelArray(gamedisplay)

for i in range(0,X):
    for j in range(0,Y):
        pixAr[i][X//2] = green
        pixAr[Y//2][j] = green
       

def plot_point(p,q):
    pixAr[(X//2)+p][(Y//2)+q] = red
    
    
def plot_text(p,q):
    
    text = font.render('({},{})'.format(p,q), True, white)
    textRect = text.get_rect()
    textRect.center = ((X//2)+(15+p), (Y//2)+(10+q))
    plot_point(p, q)
    return text,textRect

    

t,tr = plot_text(0,0)  
t1,tr1 = plot_text(10,10)  
pixAr.close()
gamedisplay.blit(t, tr)
gamedisplay.blit(t1, tr1)
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