import pygame

"""
arial_font.
          .Set_bold()
          .set_italic()
          .set_underline()
        des fonctions à appliquer sur la police de caratère charger ici c'est arial_font
"""
window_resolution = (640, 480)
blue =(0, 75,255)

pygame.init()

pygame.display.set_caption("39_affiché du texte")



surface1 =  pygame.display.set_mode(window_resolution)
pygame.display.flip()


#print(pygame.font.get_fonts())

#arial_font = pygame.font.SysFont("arial",20, True)#cette ligne permet de changer la police système arial de caratère elle doit etre fait en dehors d'une boucle,True pour gras
arial_font = pygame.font.Font("GAME ROBOT-Bold.otf",20)#pour chargé une police ficher
hello_text_surface = arial_font.render("SALUT JOHN CARLOS",True,blue)

surface1.blit(hello_text_surface, [190,10])




pygame.display.flip()



launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False



    