import pygame,random
pygame.init()

FPS = 100
clock = pygame.time.Clock()
window_width=1000
window_height=1000
gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Flappy bird')

green = (0,255,0)
black = (0, 0, 0)
white = (255,255,255)

class Ball(pygame.sprite.Sprite):
	def __init__(self,color,size,name):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((size*2,size*2))
		self.image.fill(white)
		pygame.draw.circle(self.image,color,(size,size),size,0)
		self.rect=self.image.get_rect()
		self.size = self.rect.size
		self.x_speed = 2
		self.name = name
		if self.name == 'player':
			self.rect.x = (window_width/2) - (self.size[0]/2)
			self.rect.y = (window_height/2) - (self.size[1]/2)
		if self.name == 'enemy':
			self.rect.x = (window_width) - (self.size[0])
			self.rect.y = random.randint(0,window_height)
		self.y_speed = 1

	def update(self):
		if self.name == 'enemy':
			self.rect.x -= self.x_speed


def gameloop():
	game_quit = False
	player_gp = pygame.sprite.Group()
	enemy_gp = pygame.sprite.Group()

	ball = Ball(green,10,'player')
	player_gp.add(ball)

	for i in range(5):
		obsticle = Ball(black,12,'enemy')
		enemy_gp.add(obsticle)

	while game_quit!=True:
		clock.tick(FPS)
		gameDisplay.fill(white)

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		player_gp.update()
		enemy_gp.update()
		player_gp.draw(gameDisplay)
		enemy_gp.draw(gameDisplay)

		pygame.display.flip()

gameloop()
pygame.quit()
quit()
