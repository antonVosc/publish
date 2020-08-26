import pygame,ctypes

#Init
pygame.init()
FPS = 60
clock = pygame.time.Clock()
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0)
window_height=user32.GetSystemMetrics(1)
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)
pygame.display.set_caption('Car Race')

white = (255,255,255)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/car.png') #loading an emeny car image into a project
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.y = window_height-self.size[1]

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]

def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))


def menu():
	pygame.draw.rect(gamedisplay, (0,255,0), (window_width/8, window_height/4, 300, 300), 0)
	pygame.draw.rect(gamedisplay, (0,0,255), ((window_width/2)-150, window_height/4, 300, 300), 0)
	pygame.draw.rect(gamedisplay, (255,0,0), ((window_width/8)*6, window_height/4, 300, 300), 0)
	drawtext('Play', (window_width/8)+90, (window_height/4)+90, (0,0,0), 70)
	drawtext('Stats', (window_width/2)-100, (window_height/4)+90, (0,0,0), 70)
	drawtext('Exit', ((window_width/8)*6)+85, (window_height/4)+90, (0,0,0), 70)

def gameloop():
	game_quit = False

	player_gp = pygame.sprite.Group()

	player = Player()
	player_gp.add(player)

	while game_quit!=True:
		clock.tick(FPS)
		gamedisplay.fill(white)
		menu()
		#Event handling
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		mouse_x, mouse_y = pygame.mouse.get_pos()
		if ((mouse_x > window_width/8) and (mouse_x < ((window_width/8)+300))) and ((mouse_y > window_height/4) and (mouse_y < ((window_height/4)+300))):
			pres = pygame.mouse.get_pressed()
			if pres[0]==1:
				print('Play',pres)

		player_gp.update()

		player_gp.draw(gamedisplay)

		pygame.display.flip()


gameloop()
pygame.quit()
quit()
