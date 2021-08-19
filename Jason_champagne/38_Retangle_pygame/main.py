import pygame
import time

"""
pygame.Rect(x, y, width,height)

Rect.copy()------> mynewrect= myrect.copy()
Rect.move() | Rect.move_ip()#change les coodonné
Rect.inflate() #dilacté et contracté 
"""
window_resolution = (640, 480)
red = (255, 0 ,0)
i = 0
black = (0,0,0)



pygame.init()



pygame.display.set_caption("40_event")

surface1 = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(15, 10, 250, 80)
pygame.draw.rect(surface1, red, myrect)
    
    



pygame.display.flip()

while i< 20:
    time.sleep(.065)
    surface1.fill(black)
    myrect.x += 10
    myrect.y += 10
    pygame.draw.rect(surface1,red, myrect)
    pygame.display.flip()
    i+=1


launched = True

while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

