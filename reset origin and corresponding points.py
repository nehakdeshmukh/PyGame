# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:53:30 2023

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

def setup_origin(p=None,q=None):
    if (p and q):
        X=p
        Y=q
    else:
        X=p//2
        Y=q//2
    print(X,Y)
    return X,Y

p,q = setup_origin(400,788)

for i in range(0,X):
    for j in range(0,Y):
        pixAr[p][i] = green
        pixAr[j][q] = green
       
def position(a,b,p,q):
    if((a>0) and (b>0)): 
        print("inside ++")
        pos = (p+a, q-b) 
        return a,-b,pos 
    
    elif((a<0) and (b>0)):
        print("inside -+")
        pos = (p+a, q-b)
        return a,-b,pos 
    
    elif((a<0) and (b<0)):
        print("inside --")
        pos = (p+a, q-b)
        return a,-b,pos
    
    elif((a>0) and (b<0)):
        print("inside +-")
        pos = (p+a, q-b)
        return a,-b,pos
    
    pos = (p+a, q+b)
    return a,b,pos

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