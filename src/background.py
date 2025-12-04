import pygame 

class Backgrounds(pygame.sprite.Sprite):
    def __init__(self, size, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(img), size)