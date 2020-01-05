import pygame,time
pygame.init()
window_width=1440#user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=900#user32.GetSystemMetrics(1) #getting my screen height from line 3
gamedisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('space wars') #the name of the poject (appears at the top of the game window as a name of a game)
spaceship=pygame.image.load('spaceship.png') #loading an emeny car image into a project
bg = pygame.image.load('stars.jpg')
bg = pygame.transform.scale(bg,(window_width,window_height))
spaceship_size = spaceship.get_rect().size
spaceship = pygame.transform.scale(spaceship, (int(spaceship_size[0]/12),int(spaceship_size[1]/12)))
spaceship_size = spaceship.get_rect().size

blue=(0,0,255)

class Rockets(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bullet.png")
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
		global y
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('spaceship.png') #loading an emeny car image into a project
		self.spaceship_size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image, (int(self.spaceship_size[0]/12),int(self.spaceship_size[1]/12)))
		self.spaceship_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		x=(window_width*0.5)-(self.rect.x*0.5)
		y=window_height-self.rect.y
	def draw_ship(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		gamedisplay.blit(self.image,(mouse_x,window_height-spaceship_size[1]))

def gameloop():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	game_quit = False
	all_sprites = pygame.sprite.Group()
	ship = Spaceship()
	rocket = Rockets()
	all_sprites.add(rocket)
#	all_sprites.add(ship)
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
				ship.draw_ship()
				rocket.start(mouse_x+(spaceship_size[0]/2)-13,y)
				bullet_vis=True
				print("shoot")
		rocket.shoot(bullet_vis)
		ship.draw_ship()
		all_sprites.update()
		all_sprites.draw(gamedisplay)
		pygame.display.update()

gameloop()
pygame.quit()
quit()
