import pygame
from src.player import Player
from src.exit import Exit


class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        self.player = Player(self.width // 2, self.height //2, (50, 50))
        self.exit = Exit(self.width - 15, 15)

    def mainloop(self):
        run = True
        while run == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and self.exit.exit_rect.collidepoint(event.pos):
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    print("shoot")        #must write shoot function

            # Movement Function  
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.player_hitbox.x > 0:
                self.player.left()

            if keys[pygame.K_RIGHT] and self.player.player_hitbox.right < self.width:
                self.player.right()
        
          
            self.screen.fill("black")
            self.screen.blit(self.player.player_model, self.player.player_hitbox)
            self.screen.blit(self.exit.exit_button, self.exit.exit_rect)

            pygame.display.flip()
                

        
            
            
        
        

