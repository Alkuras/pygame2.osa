import pygame
import sys
import random

def joonista_rudustik(screen,a,b,color):
    p=0
    l=0
    for k in range(surface.get_height()):
        
        for i in range(surface.get_width()):
            pygame.draw.rect(screen,color,(p,l,a,b))
            p+=25
            
        l+=25
        p=0
pygame.init()

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
varv=[r,g,b]
lgreen=[153,255,153]
red=[255,0,0]

surface=pygame.display.set_mode((640,480))
pygame.display.set_caption("Ruudustik")
surface.fill(lgreen)
joonista_rudustik(surface,23,23,varv)


pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
