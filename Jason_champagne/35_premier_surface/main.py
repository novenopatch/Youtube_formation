import pygame


"""
pour pygame.display()# (|) pour entrer plusieur paramètre
pygame.FULLSCREEN
      .RESIZABLE
      .NOFRAME
      .
      .
      .OPENGL
      .HWSURFACE # accélération matériel
      .DOUBLEBUF # double mémoire tampon passage dune image à une autre
      .


"""
res = (640, 480)


pygame.init()

pygame.display.set_caption("Pygame Test")

window_surface = pygame.display.set_mode(res )
#print(pygame.display.Info())#affiche des information sur l'affichage du programme
#print(pygame.get_sdl_version())
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

#pygame.quit()#décharger les modules chargés            