import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, img = "assets/fighter_jet.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.model = pygame.transform.scale(self.original_image, size)
        self.hitbox = self.model.get_rect()
        self.hitbox.center = (x, y)
        
    def left(self):
        self.hitbox.x -= 3

    def right(self):
        self.hitbox.x += 3
    



