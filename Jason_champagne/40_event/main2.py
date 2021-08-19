import pygame

window_resolution = (640, 480)

pygame.init()
pygame.display.set_caption("envent suite")
surface1 = pygame.display.set_mode(window_resolution,)
pygame.display.flip()


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("HAUT")
            elif event.key == pygame.K_DOWN:
                print("BAS")
            elif event.key == pygame.K_LEFT:
                print("GAUCHE")
            elif event.key == pygame.K_RIGHT:
                print("DROITE")
            else:
                print("Une autre touche")


