import pygame
import sys
import random

pygame.init()
yellow=[255,255,0]
red=[255,0,0]
green=[0,255,0]
grey=[128,128,128]
blue=[0,0,255]

surface=pygame.display.set_mode((840,680),pygame.RESIZABLE)
pygame.display.set_caption("Majake")
surface.fill(blue)

def drawhouse(x,y,width,height,screen,color):
    points=[(x,y-((3/4.0)*height)),(x,y),(x+width,y),(x+width,y-(3/4.0)*height),(x,y-((3/4.0)*height)),(x+width/2.0,y-height),(x+width,y-(3/4.0)*height)]
    
    
    lineThickness=3
    pygame.draw.lines(screen,color,False,points,lineThickness)
    
    

def drawwindow(x,y,width,height,screen,color):
    lineThickness=3
    window=[(x+width/5,y-height/1.5),(width*(3/5),y-height/1.5),(width*(3/5),y-height/2),(width*(3/5),y-height/1.5),(x+width/5,y-height/2),(x+width/5,y-height/1.5),(width*(3/5),y-height/2),(x+width/5,y-height/2)]
    pygame.draw.lines(screen,color,False,window,lineThickness)

def drawdoor(x,y,width,height,screen,color):
    lineThickness=3
    

    door=[(x+width/2,y),(width*(3/4),y),(width*(3/4),y),(width*(3/4),y-height/2),(x+width/2,y),(x+width/2,y-height/2),(width*(3/4),y-height/2),(x+width/2,y-height/2)]
    pygame.draw.lines(screen,color,False,door,lineThickness)
def drawchimney(x,y,width,height,screen,color):
    lineThickness=3
    chimney=[(x+width/3,y-((3/4.0)*height)),(x+width/3,y-height*1.5),(x+width/3,y-height*1.5),(x+width/2,y-height*1.5),(x+width/2,y-height),(x+width/2,y-height*1.5)]
    pygame.draw.lines(screen,color,False,chimney,lineThickness)

while True:
    surface.fill(blue)
    drawhouse(100,400,surface.get_width()/3,surface.get_height()/3,surface,red)
    drawwindow(100,400,surface.get_width()/3,surface.get_height()/3,surface,green)
    drawdoor(100,400,surface.get_width()/3,surface.get_height()/3,surface,yellow)
    drawchimney(100,400,surface.get_width()/3,surface.get_height()/3,surface,red)

    pygame.display.flip()

    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
