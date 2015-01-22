import pygame

#---------------------------------------------------------------------
#Running images

r1 = pygame.image.load("running/sprite_running1.png")
r2 = pygame.image.load("running/sprite_running2.png")
r3 = pygame.image.load("running/sprite_running3.png")
r4 = pygame.image.load("running/sprite_running4.png")
r5 = pygame.image.load("running/sprite_running5.png")
r6 = pygame.image.load("running/sprite_running6.png")
r7 = pygame.image.load("running/sprite_running7.png")
r8 = pygame.image.load("running/sprite_running8.png")
r9 = pygame.image.load("running/sprite_running9.png")
r10 = pygame.image.load("running/sprite_running10.png")
r11 = pygame.image.load("running/sprite_running11.png")
r12 = pygame.image.load("running/sprite_running12.png")
        
runningList = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12]

#---------------------------------------------------------------------

#----------------------------------------------------------------
#Jumping images
j1 = pygame.image.load("jumping/sprite_jumping1.png")
j2 = pygame.image.load("jumping/sprite_jumping2.png")
j3 = pygame.image.load("jumping/sprite_jumping3.png")
j4 = pygame.image.load("jumping/sprite_jumping4.png")
j5 = pygame.image.load("jumping/sprite_jumping5.png")
j6 = pygame.image.load("jumping/sprite_jumping6.png")
j7 = pygame.image.load("jumping/sprite_jumping7.png")
j8 = pygame.image.load("jumping/sprite_jumping8.png")
j9 = pygame.image.load("jumping/sprite_jumping9.png")
j10 = pygame.image.load("jumping/sprite_jumping10.png")
j11 = pygame.image.load("jumping/sprite_jumping11.png")
j12 = pygame.image.load("jumping/sprite_jumping12.png")
j13 = pygame.image.load("jumping/sprite_jumping13.png")
j14 = pygame.image.load("jumping/sprite_jumping14.png")
j15 = pygame.image.load("jumping/sprite_jumping15.png")
j16 = pygame.image.load("jumping/sprite_jumping16.png")
j17 = pygame.image.load("jumping/sprite_jumping17.png")
j18 = pygame.image.load("jumping/sprite_jumping18.png")
j19 = pygame.image.load("jumping/sprite_jumping19.png")
j20 = pygame.image.load("jumping/sprite_jumping20.png")
        
jumpingList = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]
#----------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = r1
        #self.image = pygame.Surface([50, 50])
        #self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (50, 300)
        self.in_air = False
        self.on_ground = False
        self.ticker=15
        self.frame_shift=1
        self.currentImage=1
        self.enter_jump_animation=False
        
    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def get_loc(self):
        return self.loc

    def jump(self):
        if self.in_air == False:
            self.set_pos(self.rect.x, self.rect.y-48)
        else:
            pass
        self.in_air = True

    def duck(self):
        if self.on_ground == False:
            self.set_pos(self.rect.x, self.rect.y+20)
        else:
            pass
        self.on_ground = True

    def reset(self):
        self.set_pos(50,300)

    def tick(self):
        self.ticker-=1
        if self.ticker<=0:
            self.reset()
            self.in_air = False
            self.ticker=15

    def set_jump_time(self, time):
        if self.ticker!=8:
            self.ticker=time

    def next_image(self):
        if self.in_air:
            self.enter_jump_animation=True
        if self.enter_jump_animation:
            self.frame_shift-=1
            if self.frame_shift<=0:
                if self.currentImage<19:
                    self.image=jumpingList[self.currentImage+1]
                    self.currentImage+=1
                    self.frame_shift=1
                else:
                    self.image=r1
                    self.currentImage=1
                    self.enter_jump_animation=False
        else:
            self.frame_shift-=1
            if self.frame_shift<=0:
                self.image=runningList[(runningList.index(self.image)+1)%12]
                self.frame_shift=1
            


