import pygame, sys, time
from player import *
from obstacle import *
from backgound import *
from pygame.locals import *



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Runner")
        self.screen.fill((0,0,0))

class Runner:
    def __init__(self, screen):     
        self.screen = screen
        self.screen.fill((0,100,150))
        self.playing = True
        self.speed = 10

        pygame.font.init()
        self.font = pygame.font.Font(None, 60)
        #Make and draw Player
        self.player = Player()
        self.players = pygame.sprite.Group(self.player)
        self.players.draw(self.screen)

        #Make and draw obstacles
        self.obstacle = Obstacle(self.speed)
        self.obstacles = pygame.sprite.Group(self.obstacle)
        self.obstacles.draw(self.screen)
        

        #Make background
        self.backdrop = Background(self.speed-2,0,0)
        self.backdrop2 = Background(self.speed-2,800,0)
        self.backdrops= pygame.sprite.Group(self.backdrop, self.backdrop2)
        pygame.display.flip()


    def main_loop(self):
        events = [event.type for event in pygame.event.get()]
        while pygame.QUIT not in events:
            self.screen.fill((0,100,150))
            if pygame.MOUSEBUTTONDOWN in events:
                if self.obstacle.is_up:
                    self.player.roll()
                else:
                    self.player.jump()
            #time.sleep(.01)

            #Check for collisions
            self.check_collision()
            if self.playing:
                self.update()

            #Lose condition
            else:
                ren=self.font.render("You lose! Score: " + str(run.obstacle.score)+ "   Click to restart", 0 ,(255,0,0))
                self.screen.blit(ren, (10,10))
                pygame.display.flip()

                #Restart game, reset character
                if pygame.MOUSEBUTTONDOWN in events:
                    self.playing = True
                    self.player.reset()
                    self.obstacle.reset()
                    self.obstacle.score=0
                    self.update_velocity(10)
                    print "reset"
                    
            events = [event.type for event in pygame.event.get()]
        pygame.quit()

    
    #Update the display with all of the sprites
    def update(self):
        if self.obstacle.score>5:
            self.update_velocity(15)
            if self.obstacle.score>10:
                self.update_velocity(20)
                if self.obstacle.score>20:
                    self.update_velocity(25)
        self.backdrops.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.obstacle.move()
        self.player.next_image()
        self.players.draw(self.screen)
        self.backdrop.move()
        self.backdrop2.move()
        if self.player.in_air:
            self.player.tick()
        if self.player.on_ground:
            self.player.tick()
        pygame.display.flip()

    def check_collision(self):
        if self.obstacle.rect.x+self.obstacle.WIDTH-15>self.player.rect.x and self.obstacle.rect.x<self.player.rect.x+50:
            if self.player.in_air or self.player.on_ground:
                pass
            else:
                if self.obstacle.score>0:
                    self.playing = False
        else:
            pass

    def update_velocity(self, speed):
        self.obstacle.set_vel(speed)
        self.backdrop.set_vel(speed)
        self.backdrop2.set_vel(speed)
        
    

game= Game()
run = Runner(game.screen)
run.main_loop()
print run.obstacle.score
