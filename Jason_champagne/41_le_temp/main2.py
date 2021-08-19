import pygame

#print("%.2f" % <variable à affiché>) #il permet d'avoir un affichage à deux chiffre après la virgule
#print(f"{<>:.2f}")
window_resolution = (640, 480)
blue_color = (132, 180, 255)
launched = True
red_color = (255, 0 , 0)
black_color=(0, 0, 0)
pygame.init()

clock = pygame.time.Clock()#récupère ou initilise l'objet clock

pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.display.set_caption("Python #41 - mesurer le temps")
window_surface = pygame.display.set_mode(window_resolution)


arial_font = pygame.font.SysFont("arial", 36)









while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched= False
        elif event.type == pygame.USEREVENT:#cette  condition est lié à userevent 
            #créér la haut il permet de réaliser la boucle quelle contion toute les 2ms comme définie la haut
            window_surface.fill(black_color)
            text = arial_font.render(f"{clock.get_fps():.2f} Fps!", True, blue_color)
            window_surface.blit(text, [50,50])
            pygame.display.flip()
    clock.tick(60)#30 images par seconde (30fps)
