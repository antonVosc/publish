import pygame,time,random,ctypes

#Init
pygame.init()
FPS = 60
clock = pygame.time.Clock()
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=user32.GetSystemMetrics(1) #getting my screen height from line
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Space Wars') #the name of the poject (appears at the top of the game window as a name of a game)

#Loading components
bg = pygame.image.load('images/stars.jpg')
bg = pygame.transform.scale(bg,(window_width,window_height))
asteroids = ['images/big_1.png','images/big_2.png','images/huge_1.png','images/sm_1.png','images/sm_2.png','images/sm_3.png']
smallfont = pygame.font.SysFont('comicsansms',35) #setting up the correct font and size for a score
exp_animation =[]
for i in range(1,9):
	exp_animation.append('images/exp/'+str(i)+'.png')

#Colors
black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)

def score(score):
	text=smallfont.render("Score: "+str(score),True, white)
	gamedisplay.blit(text,[0,0])

class Bullets(pygame.sprite.Sprite):
	def __init__(self,player_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/bullet.png")
		self.bullet_size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.bullet_size[0]/7),int(self.bullet_size[1]/7)))
		self.bullet_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x=player_pos.rect.x+player_pos.Player_size[0]/2-17 # player.Player_size[0]/2)-13,player.rect.y+50
		self.rect.y=player_pos.rect.y+50
		self.y_speed = -25

	def update(self):
		self.rect.y += self.y_speed
		if self.rect.y < -200:
			self.kill()


class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/spaceship.png') #loading an emeny car image into a project
		self.Player_size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.Player_size[0]/12),int(self.Player_size[1]/12)))
		self.Player_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = ((window_width*0.5)-(self.rect.x*0.5),window_height-self.Player_size[1]/2)

	def update(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.rect.x=mouse_x


class Asteroids(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(random.choice(asteroids))
		self.asteroid_size = self.image.get_rect().size
		if self.asteroid_size[0]>200:
			self.image = pygame.transform.scale(self.image, (int(self.asteroid_size[0]/2),int(self.asteroid_size[1]/2)))
			self.asteroid_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,window_width)
		self.rect.y = 0-self.asteroid_size[1]
		self.y_speed = random.randrange(1, 8)
		if self.rect.x>window_width/2:
			self.x_speed = -1
		else:
			self.x_speed = 1

	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		if window_width<self.rect.x or self.rect.x<0-self.asteroid_size[0] or window_height<self.rect.y:
			self.kill()
			asteroid=Asteroids()
			#Adding to the group
			asteroids_gp.add(asteroid)

class Explosions(pygame.sprite.Sprite):
	def __init__(self,center):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(exp_animation[0])
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_updated = pygame.time.get_ticks()
		self.anim_fps = 60

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_updated > self.anim_fps:
			self.last_updated = now
			self.frame += 1
			if self.frame == len(exp_animation):
				self.kill()
			else:
				center = self.rect.center
				self.image = pygame.image.load(exp_animation[self.frame])
				self.rect = self.image.get_rect()
				self.rect.center = center



def gameloop():
	global asteroids_gp
	my_score = 0
	game_quit = False
	clock.tick(FPS)


	#Group creation
	player_gp = pygame.sprite.Group()
	bullets_gp = pygame.sprite.Group()
	asteroids_gp = pygame.sprite.Group()
	explosion_gp = pygame.sprite.Group()

	#Object creation
	player = Player()
	for i in range(5):
		asteroid=Asteroids()
		#Adding to the group
		asteroids_gp.add(asteroid)
	player_gp.add(player)

	while game_quit!=True:
		gamedisplay.blit(bg,(0,0))
		score(my_score)

		#Event handling
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				bullet = Bullets(player)
				bullets_gp.add(bullet)

		#Collisions
		crashes = pygame.sprite.groupcollide(bullets_gp,asteroids_gp, True, True)
		for crash in crashes:
			my_score += 1
			expl = Explosions(crash.rect.center)
			explosion_gp.add(expl)
			asteroid=Asteroids()
			asteroids_gp.add(asteroid)
			if (my_score % 5) == 0:
				asteroids_gp.add(asteroid)

		death = pygame.sprite.spritecollide(player, asteroids_gp, True)
		if death:
			game_quit=True

		#Sprite Update
		player_gp.update()
		bullets_gp.update()
		asteroids_gp.update()
		explosion_gp.update()

		#Sprite Draw
		player_gp.draw(gamedisplay)
		bullets_gp.draw(gamedisplay)
		asteroids_gp.draw(gamedisplay)
		explosion_gp.draw(gamedisplay)
		pygame.display.flip()


gameloop()
pygame.quit()
quit()
