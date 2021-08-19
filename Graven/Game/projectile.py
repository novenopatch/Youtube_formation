import pygame


class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        