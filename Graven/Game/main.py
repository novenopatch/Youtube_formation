#!/usr/bin/env python3
import pygame
from game import Game

pygame.init()





running = True
screen_window = (1080, 720)
background = pygame.image.load("assets/bg.jpg")

game = Game()
#player = Player()#avant de créer la class game on a créé la class player à ce moment la on avait bésoin de d'appeler
# player dans le ficher alors que maintenant avec la class game, c'est la class game qui créé player

pygame.display.set_caption("Game")
screen = pygame.display.set_mode(screen_window, )

while running:
    screen.blit(background, [0, -200]) # la partie [0: monté, -200: monté dans l'image de moyen de 200]

    screen.blit(game.player.image, game.player.rect)
    game.player.all_projectile.draw(screen)

    for monster in game.all_monsters:
        monster.forward()
    game.all_monsters.draw(screen)


    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    #print(game.pressed)

    
    pygame.display.flip()
    # si le jouer ferme cette fenètre
    for event in pygame.event.get():
        # si evènement est fermeture de fenetre est fermé
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT
            print("Fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


