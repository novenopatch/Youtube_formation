import pygame

window_resolution = (640, 480)
while_color = (255, 255, 255)
black_color =(0,0,0)

pygame.init()

pygame.display.set_caption("40_event")
screen1 = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)


arial_font = pygame.font.SysFont("arial", 30)
#dimenssion_text = arial_font.render("{}".format(window_resolution), True, while_color)
#screen1.blit(dimenssion_text, [10,10])#pour la mettre sur la suface et la position






launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.VIDEORESIZE:
            screen1.fill(black_color)
            dimenssion_text = arial_font.render("{}x{}".format(event.w, event.h), True, while_color)
            screen1.blit(dimenssion_text, [10,10])#pour la mettre sur la suface et la position
            pygame.display.flip()


