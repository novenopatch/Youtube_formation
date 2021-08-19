import pygame

#Surface, Rect
#Rect(left(décalage), top , width, height)

resolution = (640, 480)
blue_color = (89, 152, 255)
black_color = (0,0,0)


pygame.init()

pygame.display.set_caption("Pygame Test")

window_surface = pygame.display.set_mode(resolution, )
window_surface.fill(blue_color)#definie la couleur




#pygame.draw.line(window_surface,black_color) <[10, 10], [100, 100]>taille de la ligne ,<int>épaisseur

#rect_form = pygame.Rect(100, 90, 150 , 65)#cood rectangle

#pygame.draw.rect(window_surface, black_color,rect_form, 100) #<int> epaisseur ici 100

#pygame.draw.circle(window_surface, black_color, [150, 100] , 55 , 12)# surface, couleur_de_remplissage, rayon, remplissage
#coodrs = [(10,10), (100,10), (30,50)]
#pygame.draw.polygon(window_surface,black_color,coodrs)#ici remplissage non rentré
pygame.display.flip()#correspond à update de la suface

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
