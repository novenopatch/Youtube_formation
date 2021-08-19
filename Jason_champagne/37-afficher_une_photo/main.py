import pygame

resolution = (1080, 720)
#blue_color = (89, 152, 255)


pygame.init()

pygame.display.set_caption("afficher une photo")

window_surface = pygame.display.set_mode(resolution, )
#window_surface.fill(blue_color)#definie la couleur

#le chargement des ressources se fait au debut , pas dans une boucle continue
cat_image = pygame.image.load("bg.jpg") #Retourne une surface,code a adapter pour les images dont on a pas besoin de gérer la transparence
cat_image.convert() #à utiliser pour optimiser l'affichage, pour les images à transparences: .convert_alpha()
#cat_image.set_colorkey(<nom de la variable de la couleur ciblé>)#couleur à rendre transparent sur l'image 




launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            pygame.QUIT

    window_surface.blit(cat_image,[0,-200])#les valeur de la liste permette d'ajuster l'image sur la surface(<>ajouté coté et <>profondeur)


    pygame.display.flip()#correspond à update de la suface