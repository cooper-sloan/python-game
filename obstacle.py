import pygame, random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, vel):
        self.WIDTH=25
        self.HEIGHT=25
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        #self.image.fill((0,100,0))
        self.image = pygame.image.load("spikes.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (750, 340)
        self.vel=vel
        self.score=0
        self.is_up = False

    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def get_loc(self):
        return self.loc

    def move(self):
        self.set_pos(self.rect.x-self.vel, self.rect.y)
        if self.rect.x < 0:
            i = random.random()
            print i 
            if i >= .5:
                self.switch_loc()
            self.rect.x = 850
            self.score+=1
            

    def set_vel(self, vel):
        self.vel =vel

    def reset(self):
        self.vel =10

    def switch_loc(self):
        
        if self.is_up:
            self.set_pos(self.rect.x, self.rect.y+15)
            self.is_up=False
        else:
            self.set_pos(self.rect.x, self.rect.y-15)
            self.is_up=True
