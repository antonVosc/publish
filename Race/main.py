import pygame,ctypes,random

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
		self.lives = 3
		self.score = 0

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]

class Obsticles(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.obst = ['images/cone.png','images/road-closed.png']
		self.image = pygame.image.load('{}'.format(random.choice(self.obst)))
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,window_width-self.size[0])
		self.rect.y = self.size[1] * -1

	def update(self):
		self.rect.y += 5
		if self.rect.y > window_height:
			player.score += 1
			self.kill()


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))


def menu():
	pygame.draw.rect(gamedisplay, (0,255,0), (window_width/8, window_height/4,300,300), 0)
	pygame.draw.rect(gamedisplay, (0,0,255), ((window_width/2)-150, window_height/4, 300, 300), 0)
	pygame.draw.rect(gamedisplay, (255,0,0), ((window_width/8)*6, window_height/4, 300, 300), 0)
	drawtext('Play', (window_width/8)+90, (window_height/4)+90, (0,0,0), 70)
	drawtext('Stats', (window_width/2)-100, (window_height/4)+90, (0,0,0), 70)
	drawtext('Exit', ((window_width/8)*6)+85, (window_height/4)+90, (0,0,0), 70)

def gameloop():
	global obsticles_gp,player

	game_quit = False

	player_gp = pygame.sprite.Group()
	player = Player()
	player_gp.add(player)

	obsticles_gp = pygame.sprite.Group()
	obst = Obsticles()
	obsticles_gp.add(obst)

	but_size = 300
	start_but_coords = (window_width/8,window_height/4,(window_width/8)+but_size,(window_height/4)+but_size)
	stats_but_coords = ((window_width/2)-150,window_height/4,((window_width/2)-150)+but_size,(window_height/4)+but_size)
	ext_btn_coords = ((window_width/8)*6,window_height/4,((window_width/8)*6)+but_size,(window_height/4)+but_size)
	start_game = False
	display_menu = True
	stats = False

	while game_quit!=True:
		clock.tick(FPS)
		gamedisplay.fill(white)

		#Event handling
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		if display_menu == True:
			menu()
		else:
			player_gp.draw(gamedisplay)
			player_gp.update()
			obsticles_gp.draw(gamedisplay)
			obsticles_gp.update()
			drawtext('Lives: '+str(player.lives), 0,0, (0,0,0), 70)
			drawtext('Score: '+str(player.score), window_width-350,0, (0,0,0), 70)

		if stats == True:
			gamedisplay.fill(white)

		prob = random.randint(0,1000)
		if prob <= 20:
			obsticle = Obsticles()
			obsticles_gp.add(obsticle)

		collision = pygame.sprite.groupcollide(player_gp,obsticles_gp,False,True)
		if collision:
			player.lives -= 1

		if player.lives == 0:
			pygame.quit()
			quit()

		mouse_x, mouse_y = pygame.mouse.get_pos()
		if ((mouse_x > start_but_coords[0]) and (mouse_x < start_but_coords[2])) and ((mouse_y > start_but_coords[1]) and (mouse_y < start_but_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0]==1:
				display_menu = False


		if ((mouse_x > ext_btn_coords[0]) and (mouse_x < ext_btn_coords[2])) and ((mouse_y > ext_btn_coords[1]) and (mouse_y < +ext_btn_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0] == 1:
				pygame.quit()
				quit()

		if ((mouse_x > stats_but_coords[0]) and (mouse_x < stats_but_coords[2])) and ((mouse_y > stats_but_coords[1]) and (mouse_y < stats_but_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0]==1:
				stats=True

		pygame.display.flip()


gameloop()
pygame.quit()
quit()
