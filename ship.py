import pygame
from settings import Settings
class Ship():
    #ship control
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,(50, 45))
        self.rect = self.image.get_rect()
        
        self.settings = ai_game.settings

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    
    def update(self):
        #Update x atribute not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #if self.moving_right and self.rect.right < self.screen_rect.right:
        #    self.x += self.settings.ship_speed
        #if self.moving_left and self.rect.left > 0:

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
