import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,vel,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.png").convert_alpha()
        #self.image = pygame.Surface([50, 50])
        #self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.vel=vel
        
    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def get_loc(self):
        return self.loc

    def move(self):
        self.set_pos(self.rect.x-self.vel, self.rect.y)
        if self.rect.x <= -800:
            self.rect.x = 800
            
    def set_vel(self, vel):
        self.vel =vel
