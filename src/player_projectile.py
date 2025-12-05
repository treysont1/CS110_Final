import pygame

class Player_Projectile(pygame.sprite.Sprite):
    def __init__(self, bottomy, midx = 0, leftx = 0, rightx = 0, width = 0, img = "assets/player_projectile.png"):
        super().__init__()
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.original_image, (9, 25))
        self.rect = self.image.get_rect()
        if midx != 0:
            self.rect.midbottom = (midx, bottomy)
        if leftx != 0:
            self.rect.bottomleft = (leftx, bottomy)
        if rightx != 0:
            self.rect.bottomright = (rightx, bottomy)
    
    def update(self, screen, dt):
        self.rect.centery -= 1 * dt / 2
        if not screen.get_rect().contains(self.rect):
            self.kill()



