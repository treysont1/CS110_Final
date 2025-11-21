import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, img = "assets/fighter_jet.png"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.player_model = pygame.transform.scale(self.image, size)
        self.player_hitbox = self.player_model.get_rect()
        self.player_hitbox.center = (x, y)
        
    def left(self):
        self.player_hitbox.x -= 3

    def right(self):
        self.player_hitbox.x += 3
