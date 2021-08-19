import pygame


window_resolution = (640, 480)
blue_color = (132, 180, 255)
launched = True
red_color = (255, 0 , 0)
pygame.init()
pygame.display.set_caption("Python #41 - mesurer le temps")
window_surface = pygame.display.set_mode(window_resolution)


arial_font = pygame.font.SysFont("arial", 36)

text = arial_font.render("Je dois aller me laver !", True, blue_color)
window_surface.blit(text, [50,50])
pygame.display.flip()


pygame.time.wait(2000)#un équivalant de time.sleep(), avec le module time , le parmètre temps prend des valeur en miliseconde
#pygame.time.delay(2000)#ici c'est le processeur qui le fait,c'est une pause forcé!

text = arial_font.render("Je dois aller me laver !", True, red_color)
window_surface.blit(text, [50,50])

pygame.display.flip()


#print(pygame.time.get_ticks())#affiche le temps depuis l'initilisation




while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched= False
        
