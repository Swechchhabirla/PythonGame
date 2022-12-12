#import Liberary
import pygame
from pygame.locals import *
import random
pygame.init()

#set display size
display_screen = pygame.display.set_mode((700, 700))

# Game Element 
rabbit = "r" 
carrot = "c"
rabbithole = "o"
pathway1= "_ "*22
caprabbit="R"
pathway2="_ "*10
pathway3="_ "*10
pathway4="_ "*5

#text font 
font = pygame.font.SysFont(None, 20)

#set text colour
Rabbit = font.render(rabbit, True, (240, 240, 240))
Carrot = font.render(carrot, True, (240, 240, 240))
Rabbithole= font.render(rabbithole, True, (240, 240, 240))
Pathway1= font.render(pathway1, True, (240, 240, 240))
CapRabbit= font.render(caprabbit, True, (240, 240, 240))
Pathway2= font.render(pathway2, True, (240, 240, 240))
Pathway3= font.render(pathway3, True, (240, 240, 240))
Pathway4= font.render(pathway4, True, (240, 240, 240))

#initialize game element position

block_a= 382
block_b= 132
block_c= 500
block_d= 140
block_e= 20
block_f= 390
block_g= 510
block_h= 382
y_block=20

#condition 

running = True
while running:
    
     
    for event in pygame.event.get():
       
        
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                # if user press a and rabbit is lessthan carrot then continiue run rabbit when press a key    
                if event.key == K_a and block_b<=370 :
                     block_b += 10
                # if user press a and rabbit is greaterthan carrot and lessthan rabbithole then continiue run rabbit when press a key     
                if event.key == K_a and block_b>=382 and block_b<=490:
                   
                    block_b += 10
                # if user press a and rabbit is greaterthan rabithole and lessthan pathway then continiue run rabbit when press a key        
                if event.key == K_a and block_b>=510 and block_b<=553 :
                     block_b+= 10
                # if user press p rabbit pick up carrot and converted R   
                if event.key==K_p  and block_b>=370:
                     if event.key==K_p and block_b<=380:
                         block_b +=10

                # if user press d rabbit back 
                         
                if event.key ==K_d and block_b>=20 :
                    block_b -=10
                if event.key ==K_d and block_b<=510 and block_b>=500:
                    block_b -=0
                # if user press a rabbit is greaterthan pathway and lessthan ranithole then rabbit is not move
                if event.key == K_a and block_b>=490 and block_b<=510:
                        block_b += 0
                # if user press j rabbit jump o  
                if event.key==K_j and block_b<=510:
                     if event.key==K_j and block_b>=490:
                         block_b+=20
                if event.key ==K_d and block_b<=510 and block_b>=500:
                      block_b-=20
              
                      
                
                elif event.type == QUIT:
                     running = False
                    
                
                
             
                
            
           

            
 
    # Add background color to the window screen
    
    display_screen.fill((0,0,0))
    #display text with position to the window screen
    display_screen.blit(Rabbit,(block_b,y_block))
    display_screen.blit(Carrot,(block_a,y_block))
    display_screen.blit(Rabbithole,(block_c,y_block))
    display_screen.blit(Pathway1,(block_d,y_block))
    display_screen.blit(Pathway2,(block_e,y_block))
    display_screen.blit(Pathway3,(block_f,y_block))
    display_screen.blit(Pathway4,(block_g,y_block))
    
    # if rabbit and carrot same position than convert in R and rabbit and carrot colour is 0 else show rabbit and carrot 
    if block_b==block_a :
       
          display_screen.blit(CapRabbit, (block_h,y_block))
          Rabbit= font.render(rabbit, True, (0, 0, 0))
          Carrot= font.render(carrot, True, (0, 0, 0))
   
    else:
        Rabbit= font.render(rabbit, True, (240, 240, 240))
        Carrot= font.render(carrot, True, (240, 240, 240))
    # update display
    pygame.display.update()

pygame.quit()


