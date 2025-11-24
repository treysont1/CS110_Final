import pygame
from src.player import Player


class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(size = (800, 700))
        self.width, self.height = pygame.display.get_window_size()
        self.player = Player(self.width // 2, self.height //2, (50, 50))

    def mainloop(self):
        run = True
        while run == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    print("shoot")        #must write shoot function

            # Movement Function  
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.player_hitbox.x > 0:
                self.player.left()

            if keys[pygame.K_RIGHT] and self.player.player_hitbox.right < self.width:
                self.player.right()
        
          
            self.screen.fill("white")
            self.screen.blit(self.player.player_model, self.player.player_hitbox)

            pygame.display.flip()
                

        
            
            
        
        

