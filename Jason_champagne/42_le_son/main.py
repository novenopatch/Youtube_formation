import pygame
"""
<Sound>.play(loop=0, time = <ms>, fadein =<fondu>)
       .paly(1, 900, 5000)
       ce sont des paramètre optionelle
       .stop()
       .fadeout(ms)
       .set_volume(0.0 --> 1.0)
       .get_volume()
       .get_lenght()
"""

window_resolution = (640, 480)
launched = True
red_color = (255, 0 , 0)
black_color=(0, 0, 0)


pygame.init()
pygame.display.set_caption("Python #42 - le son")
window_surface = pygame.display.set_mode(window_resolution)

game_over = pygame.mixer.Sound("game_over.ogg")
métorite = pygame.mixer.Sound("meteorite.ogg")
game_over.play()
métorite.play()

pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                pygame.mixer.pause()
            if event.key == pygame.K_b:
                pygame.mixer.unpause()
            if event.key == pygame.K_SPACE:  
                game_over.stop()
            if event.key == pygame.K_DOWN or pygame.K_UP:
                pygame.mixer.stop()
