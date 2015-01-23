import pygame, sys, time, pygame.mixer
from player import *
from obstacle import *
from backgound import *
from game_menu import *
from pygame.locals import *

#----------------------------------------------------------
#Sound Effects
pygame.mixer.init()
runningSound = pygame.mixer.Sound('runninggrass.wav')
jumpingSound = pygame.mixer.Sound('jumpingSound.wav')
rollingSound = pygame.mixer.Sound('rollingSound.wav')
losingSound = pygame.mixer.Sound('jab.wav')

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Runner")
        self.screen.fill((0,0,0))

class Runner:
    def __init__(self, screen, difficulty):     
        self.screen = screen
        self.screen.fill((0,100,150))
        self.playing = True
        self.speed = 10
        self.difficulty = difficulty

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
        self.playLose = False


    def main_loop(self):
        events = [event.type for event in pygame.event.get()]
        self.update_velocity(10*self.difficulty)
        while pygame.QUIT not in events:
            self.screen.fill((0,100,150))
            if pygame.KEYDOWN in events:
                if event.key == pygame.K_DOWN and not (self.player.in_air or self.player.on_ground):
                    rollingSound.play()
                    self.player.roll()
                    runningSound.stop()
                elif event.key == pygame.K_UP and not (self.player.in_air or self.player.on_ground):
                    jumpingSound.play()
                    self.player.jump()
                    runningSound.stop()
            elif pygame.KEYUP in events and self.playing:
                runningSound.play()
            
            time.sleep(.01)
            
            #Check if sound is playing
            if self.playLose:
                self.playLose = False
                losingSound.play()
            
            #Check for collisions
            self.check_collision()
            if self.playing:
                self.update()

            #Lose condition
            else:

                #losingSound.play()
                runningSound.stop()
                print run.obstacle.score

                self.difficulty = lose(run.obstacle.score)
                print self.difficulty
                restart_main_loop(self.difficulty)
                
                """
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
                
                
                """

            events = [event.type for event in pygame.event.get()]
        pygame.quit()

    
    #Update the display with all of the sprites
    def update(self):
        z = self.obstacle.score
        if z > 5:
            self.update_velocity(10 + (.7)*z*self.difficulty)
        """
        if self.obstacle.score>5:
            self.update_velocity(15)
            if self.obstacle.score>10:
                self.update_velocity(20)
                if self.obstacle.score>20:
                    self.update_velocity(25)
        """
        self.backdrops.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.obstacle.move()
        self.player.next_image()
        self.players.draw(self.screen)
        self.backdrop.move()
        self.backdrop2.move()
        ren=self.font.render("Score: " + str(run.obstacle.score)+ " ", 0 ,(255,255,255))
        self.screen.blit(ren, (15,15))
        if self.player.in_air:
            self.player.tick()
        if self.player.on_ground:
            self.player.tick()
        pygame.display.flip()

    def check_collision(self):
        if self.obstacle.rect.x+self.obstacle.WIDTH-15>self.player.rect.x and self.obstacle.rect.x<self.player.rect.x+50:
            if self.player.in_air and not self.obstacle.is_up and self.obstacle.score>0:
                pass
            elif self.player.on_ground and self.obstacle.is_up and self.obstacle.score >0:
                pass
            else:   
                if self.obstacle.score>0:
                    self.playLose = True
                    self.playing = False
        else:
            pass

    def update_velocity(self, speed):
        self.obstacle.set_vel(speed)
        #self.backdrop.set_vel(speed)
        #self.backdrop2.set_vel(speed)

def lose(score):
	lose_options = ('Game Over', 'Your Score is ' + str(score), 'Regular', 'Hard', 'Extreme', 'QUIT')
	functions = {'Game Over': Pass, 'Regular': Pass, 'Hard': Pass, 'Extreme': Pass, 'QUIT': sys.exit}
	lose_menu = Menu(screen, lose_options, functions, score)
	difficulty = lose_menu.menu_intro()
	return difficulty

def restart_main_loop(difficulty):
	run2 = Runner(game.screen, difficulty)
	run2.main_loop()



intro = Menu(screen, menu_options, functions, 0)
difficulty = intro.menu_intro()
game= Game()
print difficulty
run = Runner(game.screen, difficulty)
run.main_loop()
print run.obstacle.score

