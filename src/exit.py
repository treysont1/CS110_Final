import pygame

class Exit:
    def __init__(self, x, y, img = "assets/exit_icon.png"):
        self.exit_button = pygame.image.load(img)
        self.exit_rect = self.exit_button.get_rect()
        self.exit_rect.center = (x, y)

