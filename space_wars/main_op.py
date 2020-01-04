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

	def shoot(self,vis):
		print(self.rect.y)
		if vis == True:
			self.y_speed = 1
		if self.rect.y > 0:
			self.y_speed = 0

	def start(self,x,y):
		self.rect.x=x
		self.rect.y=y

def draw_ship(x,y):
	gamedisplay.blit(spaceship,(x,y))

def gameloop():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	x=(window_width*0.5)-(spaceship_size[0]*0.5)
	y=window_height-spaceship_size[1]
	game_quit = False
	all_sprites = pygame.sprite.Group()
	rocket = Rockets()
	all_sprites.add(rocket)
	rocket.start(mouse_x,mouse_y)
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
				bullet_vis=True
		rocket.shoot(bullet_vis)
		draw_ship(mouse_x,y)
		all_sprites.update()
		all_sprites.draw(gamedisplay)
		pygame.display.update()
gameloop()
pygame.quit()
quit()
