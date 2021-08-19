import pygame

pygame.init()#initialise les modules de base pygame


screen = pygame.display.set_mode((640, 480))#initialise la fenetre


launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False