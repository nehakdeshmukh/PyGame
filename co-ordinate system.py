# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:59:38 2023

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
       

def position(a,b,X,Y):
    if((a>0) and (b>0)):
        print("inside ++")
        pos = ((X//2)+a, (Y//2)-b)
        return a,-b,pos # 1st 
    
    elif((a<0) and (b>0)):
        print("inside -+")
        pos = ((X//2)+a, (Y//2)-b)
        return a,-b,pos # 2nd 
    
    elif((a<0) and (b<0)):
        print("inside --")
        pos = ((X//2)+a, (Y//2)-b)
        return a,-b,pos
    
    elif((a>0) and (b<0)):
        print("inside +-")
        pos = ((X//2)+a, (Y//2)-b)
        return a,-b,pos
    
    pos = ((X//2)+(a), (Y//2)+(b))
    return a,b,pos

def plot_point(p,q):
    pixAr[(X//2)+p][(Y//2)+q] = red
    
def plot_text(p,q,X,Y):
    print(p,q) 
    l,m,pos = position(p,q,X,Y) 
    print(l,m,pos)
    text = font.render('({},{})'.format(p,q), True, white)
    textRect = text.get_rect()
    textRect.center = pos
    plot_point(l,m)
    return text,textRect


t2,tr2 = plot_text(50,-50,X,Y)  
t3,tr3 = plot_text(-50,50,X,Y)  
t4,tr4 = plot_text(-50,-50,X,Y)  
t1,tr1 = plot_text(50,50,X,Y)  
t,tr = plot_text(0,0,X,Y)  
pixAr.close()
gamedisplay.blit(t, tr)
gamedisplay.blit(t1, tr1)
gamedisplay.blit(t2, tr2)
gamedisplay.blit(t3, tr3)
gamedisplay.blit(t4, tr4)


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