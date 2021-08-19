import pygame
import time


window_resolution = (640, 480)
red = (255, 0 ,0)
i = 0
black = (0,0,0)
blue = (0,75, 255)

pygame.init()

pygame.display.set_caption("40_event")
surface1 = pygame.display.set_mode(window_resolution)


myrect = pygame.Rect(10,100,25 , 25)
myblock = pygame.Rect(600, 50, 20, 300)
pygame.draw.rect(surface1,red,myrect)
pygame.draw.rect(surface1,blue,myblock)

pygame.display.flip()



launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    
    while not myrect.colliderect(myblock):#tant qu'il ne se touche pas la boucle continue
        time.sleep(.010)
        surface1.fill(black)
        pygame.draw.rect(surface1,blue,myblock)
        myrect.x += 1
        pygame.draw.rect(surface1,red,myrect)
        pygame.display.flip()
