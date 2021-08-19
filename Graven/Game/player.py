import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.vie = 100
        self.max_vie = 100
        self.player_velocity = 5
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        Projectile = Projectile()
        self.all_projectile.add(Projectile)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
          self.rect.x += self.player_velocity
    def move_left(self):
        self.rect.x -= self.player_velocity


