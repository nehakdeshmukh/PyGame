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

p,q = setup_origin(400,600)

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

def plot_point(v,w):
    pixAr[p+v][q+w] = red
    
def plot_text(c,d,p,q):
    print(c,d) 
    l,m,pos = position(c,d,p,q) 
    print(l,m,pos)
    text = font.render('({},{})'.format(c,d), True, white)
    textRect = text.get_rect()
    textRect.center = pos
    plot_point(l,m)
    return text,textRect    

t2,tr2 = plot_text(100,-50,p,q)  
t3,tr3 = plot_text(-100,50,p,q)  
t4,tr4 = plot_text(-100,-50,p,q)  
t1,tr1 = plot_text(100,50,p,q)  
t,tr = plot_text(0,0,p,q)  
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