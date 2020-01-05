import pygame,time,random
pygame.init()
window_width=1440#user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=900#user32.GetSystemMetrics(1) #getting my screen height from line 3
gamedisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('space wars') #the name of the poject (appears at the top of the game window as a name of a game)
bg = pygame.image.load('images/stars.jpg')
bg = pygame.transform.scale(bg,(window_width,window_height))
asteroids = ['images/big_1.png','images/big_2.png','images/huge_1.png','images/sm_1.png','images/sm_2.png','images/sm_3.png']


blue=(0,0,255)

class Rockets(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/bullet.png")
		self.bullet_size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.bullet_size[0]/7),int(self.bullet_size[1]/7)))
		self.bullet_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = (-500,-500)
		self.y_speed = 0

	def update(self):
		self.rect.y += self.y_speed

	def shoot(self,vis):
		if vis == True:
#			print(self.rect.y)
			self.y_speed = -5
		if self.rect.y < -200:
			self.kill()

	def start(self,x,y):
		self.rect.x=x
		self.rect.y=y

class Spaceship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/spaceship.png') #loading an emeny car image into a project
		self.spaceship_size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.spaceship_size[0]/12),int(self.spaceship_size[1]/12)))
		self.spaceship_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = ((window_width*0.5)-(self.rect.x*0.5),window_height-self.spaceship_size[1]/2)
		self.x_speed = 0

	def draw_ship(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.rect.x=mouse_x

class Asteroids(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(random.choice(asteroids))
		self.asteroid_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
		speed=[1,-1]
		self.x_speed = random.choice(speed)
		self.y_speed = -1
		self.rect.x = random.randint(0-self.asteroid_size[0],window_width+self.asteroid_size[0])
		self.rect.y = 0-self.asteroid_size[1]
		if self.rect.x>window_width/2:
			self.x_speed = -1
		else:
			self.x_speed = 1

	def move(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed

def gameloop():
#	mouse_x, mouse_y = pygame.mouse.get_pos()
	game_quit = False
	all_sprites = pygame.sprite.Group()
	player = pygame.sprite.Group()
	ship = Spaceship()
	rocket = Rockets()
	asteroid = Asteroids()
	all_sprites.add(rocket)
	all_sprites.add(asteroid)
	player.add(ship)
	bullet_vis = False
	while game_quit!=True:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		gamedisplay.blit(bg,(0,0))
		for event in pygame.event.get(): #check every key I press
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE: ##what happens if I press Esc key
					pygame.quit() #close the game window
					quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				rocket = Rockets()
				all_sprites.add(rocket)
				rocket.start(mouse_x+(ship.spaceship_size[0]/2)-13,ship.rect.y+50)
				bullet_vis=True
		ship.draw_ship()
		rocket.shoot(bullet_vis)
		asteroid.move()
		all_sprites.update()
		player.update()
		all_sprites.draw(gamedisplay)
		player.draw(gamedisplay)
		pygame.display.flip()

gameloop()
pygame.quit()
quit()
