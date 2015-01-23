import pygame, sys


class MenuOption(pygame.font.Font):
	def __init__(self, option, font = None, font_size = 80, font_color = (0,0,0), (x, y) = (0,0)):
		pygame.font.Font.__init__(self, font, font_size)
		self.option = option
		self.font_color = font_color
		self.font_size = font_size
		self.label = self.render(self.option, 1, self.font_color)
		self.width = self.label.get_rect().width
		self.height = self.label.get_rect().height
		self.dimen = (self.width, self.height)
		self.x = x
		self.y = y
		self.xy = x, y

	def setxy(self, x, y):
		self.xy = (x, y)
		self.x = x
		self.y = y

	def set_font_color(self, rgb):
		self.font_color = rgb
		self.label = self.render(self.option, 1, self.font_color)

	def mouseover(self, (x, y)):
		if (x >= self.x and x <= self.x + self.width) and (y >= self.y and y <= self.y + self.height):
			return True
		else:
			return False


class Menu():
	def __init__(self, screen, options, functions, score, background_color = (0,0,0), font = None, font_size = 80, font_color = (255,255,255)):
		pygame.init()
		self.menu_background = pygame.image.load("menu_background.png").convert()

		self.screen = screen
		self.screen_height = self.screen.get_rect().height
		self.screen_width = self.screen.get_rect().width

		self.background_color = background_color
		self.clock = pygame.time.Clock()

		self.options = options
		self.font = pygame.font.SysFont(font,font_size)
		self.font_color = font_color
		self.score = score

		self.difficulty = 1
		self.functions = functions
		self.options = []
		for i, option in enumerate(options):
			menu_options = MenuOption(option)
			
			options_length = len(options) * menu_options.height

			y = 200 + (i * 2) + (i * menu_options.height) - (options_length/2)
			x = 400 - (menu_options.width/2)

			menu_options.setxy(x,y)
			self.options.append(menu_options)


	def menu_intro(self):
		
		game_intro = True
		while game_intro == True:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_intro = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouseposition = pygame.mouse.get_pos()
					for selection in self.options:
						if selection.mouseover(mouseposition):
							game_intro = False
							selecting = True
							while selecting:
								if selection.option == 'Regular':
									self.difficulty = 1
									selecting = False
								elif selection.option == 'Hard':
									self.difficulty = 3
									selecting = False
								elif selection.option == 'Extreme':
									self.difficulty = 5
									selecting = False
								elif selection.option == 'QUIT':
									sys.exit()
									game_intro = False
								else:
									selecting = False
									game_intro = True
								return self.difficulty
							self.functions[selection.option]()

							

			#self.screen.fill(self.background_color)
			screen.blit(self.menu_background, [0,0])

			for i in self.options:
				if i.mouseover(pygame.mouse.get_pos()):
					i.set_font_color((255,0,0))
					i.set_italic(True)
				else:
					i.set_font_color((255,255,255))
					i.set_italic(False)
				self.screen.blit(i.label, i.xy)

			pygame.display.flip()

	def get_difficulty(self):
		return self.difficulty

	def lose_game(self, score):
		self.lose_options = ('Game Over', 'Your Score is ' + str(score), 'Regular', 'Hard', 'Extreme', 'QUIT')
		self.functions = {'Regular': Pass, 'Hard': Pass, 'Extreme': Pass, 'QUIT': sys.exit}
		self.lose_menu = Menu(screen, self.lose_options, self.functions)
		self.difficulty = self.lose_menu.menu_intro()

def Pass():
	pass

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
#screen.fill((0,0,0))
menu_options = ('Regular', 'Hard', 'Extreme', 'QUIT')
functions = {'Regular': Pass, 'Hard': Pass, 'Extreme': Pass, 'QUIT': sys.exit}

#intro = Menu(screen, menu_options, functions, 0)
#intro.menu_intro()