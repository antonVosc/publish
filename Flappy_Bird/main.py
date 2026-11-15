import pygame,random,time
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
	def __init__(self,color,size,name,x_speed):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((size*2,size*2))
		self.image.fill(white)
		pygame.draw.circle(self.image,color,(size,size),size,0)
		self.rect=self.image.get_rect()
		self.size = self.rect.size
		self.x_speed = x_speed
		self.name = name
		if self.name == 'player':
			self.rect.x = (window_width/2) - (self.size[0]/2)
			self.rect.y = (window_height/2) - (self.size[1]/2)
		if self.name == 'enemy':
			self.rect.x = (window_width) - (self.size[0])
			self.rect.y = random.randint(0,window_height-self.size[1])
		self.y_speed = 1


	def update(self):
		if self.name == 'enemy':
			self.rect.x -= self.x_speed



def drawtext(text, x, y, color, size):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text,False, color)
    gameDisplay.blit(textsurface,(x, y))


def game_over(secs):
	gameDisplay.fill(white)
	drawtext('Game over.', (window_width/2)-150, (window_height/2)-150, green, 50)
	drawtext('You have managed to survive for '+str(secs)+' seconds', (window_width/2)-350, (window_height/2)-50, green, 35)
	pygame.display.flip()
	time.sleep(10)
	pygame.quit()


def gameloop():
	game_quit = False
	obs_speed = 1
	dir = -2
	start_time = pygame.time.get_ticks()

	player_gp = pygame.sprite.Group()
	enemy_gp = pygame.sprite.Group()
	ball = Ball(green,10,'player',0)
	player_gp.add(ball)

	while game_quit!=True:
		clock.tick(FPS)
		now = pygame.time.get_ticks()
		seconds = (now-start_time) // 1000

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key==pygame.K_SPACE:
					dir = 6
			if event.type == pygame.KEYUP:
				if event.key==pygame.K_SPACE:
					dir = -2

		ball.rect.y -= dir
		obs_speed += 0.001
		#crash check
		crash = pygame.sprite.groupcollide(player_gp,enemy_gp,False,False)
		if crash:
			finish = pygame.time.get_ticks()
			seconds = (finish-start_time) // 1000
			game_over(seconds)
		#top and bot check
		if ball.rect.y < 0 or ball.rect.y > window_height:
			finish = pygame.time.get_ticks()
			seconds = (finish-start_time) // 1000
			game_over(seconds)
		#new spawn
		prob = random.randint(0,100)
		if prob <= 5:
			obsticle = Ball(black,12,'enemy',obs_speed)
			enemy_gp.add(obsticle)
		# frame update
		player_gp.update()
		enemy_gp.update()
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, (255,0,0), (-6, 0, window_width+12, window_height) ,5)
		player_gp.draw(gameDisplay)
		enemy_gp.draw(gameDisplay)
		drawtext('Time: '+str(seconds), (window_width/2)-500, 0, green, 35)
		pygame.display.flip()

gameloop()
pygame.quit()
quit()
