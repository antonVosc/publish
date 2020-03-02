import pygame,time,random,ctypes

#Init
pygame.init()
FPS = 60

clock = pygame.time.Clock()
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=user32.GetSystemMetrics(1) #getting my screen height from line
gameDisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Arcanoid') #the name of the poject (appears at the top of the game window as a name of a game)
gap = window_width/120

bg = pygame.image.load('images/background.png')
bg = pygame.transform.scale(bg,(window_width,window_height))
game_over_anime = []
for i in range(1,26):
	game_over_anime.append('images/game over/game over '+str(i)+'.png')
smallfont = pygame.font.SysFont('comicsansms',75) #setting up the correct font and size for a score

white = (255,255,255)
red = (255,0,0)

def score(score): #a function for displaying the score on the screen
	text=smallfont.render("Score: "+str(score),True, white) #set up the text with the font in black colour
	gameDisplay.blit(text,[0,0]) #showing the  on the up left side of the screen

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/platform.png')
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = ((window_width/2)-(self.size[0]/2),window_height-self.size[1])
		self.speed = 0
		self.score = 0

	def update(self):
		self.rect.x += self.speed
		if self.rect.x+self.size[0] < 0:
			self.rect.x = window_width
		if self.rect.x>window_width:
			self.rect.x = 0-self.size[0]

class Ball(pygame.sprite.Sprite):
	def __init__(self,player):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/ball.png')
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/12),int(self.size[1]/12)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.center = (player.rect.center[0],player.rect.center[1])
		self.space_flag = 0
		self.y_speed = 10
		self.x_speed = 0

	def update(self,player,player_gp,ball_change):
		if self.space_flag == 0:# moving with player
			self.rect.x = player.rect.center[0]-(self.size[0]/2)
			self.rect.y = player.rect.y-45
		elif self.space_flag == 1:#when space presses
			self.space_flag=3
			self.rect.y -= self.y_speed
			self.x_speed = random.randint(-12,12)
		else:#bounce from edge
			self.rect.y -= self.y_speed
			self.rect.x -= self.x_speed
		if self.rect.x <0 or self.rect.x+self.size[0]>window_width:
			self.x_speed =- self.x_speed
		if self.rect.y <0:
			self.y_speed =- self.y_speed
		if self.rect.y>(player.rect.y-player.size[1]/1) and self.rect.y < player.rect.y+player.size[1]:
			if self.rect.x>player.rect.x and self.rect.x+self.size[0]<player.rect.x+player.size[0]:
				self.rect.y=player.rect.y-45
				self.y_speed =- self.y_speed

class Block(pygame.sprite.Sprite):
	def __init__(self,x_position,y_position):
		pygame.sprite.Sprite.__init__(self)
		self.x_position = x_position
		self.y_position = y_position
		self.image=pygame.image.load('images/{}.png'.format(random.randint(1,4)))
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/2),int(self.size[1]/2)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = window_width/12+(self.size[0]+gap)*x_position
		self.rect.y = window_height/12+(self.size[1]+gap)*y_position
		self.b_y_top = self.rect.y
		self.b_y_bot = self.rect.y+self.size[1]
		self.b_x_l = self.rect.x
		self.b_x_r = self.rect.x + self.size[0]

	def update(self,ball,ball_gp,player):
		ball.p_y_top = ball.rect.y - (ball.size[1] * 0.5)
		ball.p_y_bot = ball.rect.y + (ball.size[1] * 0.5)
		ball.p_x_l = ball.rect.x - (ball.size[0] * 0.5)
		ball.p_x_r = ball.rect.x + (ball.size[0] * 0.5)
		#if (self.b_y_bot>ball.p_y_top and self.b_y_top<ball.p_y_top) and (ball.p_x_r>self.b_x_l and ball.p_x_l<self.b_x_r):
			#ball.y_speed = ball.y_speed * -1
		collide = pygame.sprite.spritecollide(self,ball_gp,False)
		if collide:
			if self.b_x_r<ball.p_x_l or self.b_x_l>ball.p_x_r:
				ball.x_speed = ball.x_speed * -1
			else:
				ball.y_speed = ball.y_speed*-1
		#	ball.x_speed = ball.x_speed*-1

			player.score += 1
			self.kill()
		#if (self.b_x_l < ball.p_x_r) and ((self.b_y_bot>ball.p_y_bot) and (self.b_y_top<ball.p_y_top)):
		#	ball.x_speed = ball.x_speed * -1
		#	self.kill()
		#if (self.b_x_r > ball.p_x_l) and ((self.b_y_bot>ball.p_y_bot) and (self.b_y_top<ball.p_y_top)):
		#	ball.x_speed = ball.x_speed * -1
		#	self.kill()

class Gameover(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(game_over_anime[5])
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(window_width,window_height))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.frame = 0
		self.last_updated = pygame.time.get_ticks()
		self.anim_fps = 60

	def update(self, created):
		now = pygame.time.get_ticks()
		if now - self.last_updated > self.anim_fps:
			self.last_updated = now
			self.frame += 1
			center = self.rect.center
			self.image = pygame.image.load(game_over_anime[self.frame])
			self.image = pygame.transform.scale(self.image,(window_width,window_height))
			self.size = self.image.get_rect().size
			self.rect = self.image.get_rect()
			self.rect.center = center
			if self.frame == len(game_over_anime)-1:
				self.frame = 0

def gameloop():
	game_quit = False

	player_gp = pygame.sprite.Group()
	ball_gp = pygame.sprite.Group()
	blocks_gp = pygame.sprite.Group()
	game_over_gp = pygame.sprite.Group()

	player = Player()
	player_gp.add(player)

	ball = Ball(player)
	ball_gp.add(ball)

	for y in range(3):
		for i in range(15):
			block = Block(i,y) #i=x_x_position
			blocks_gp.add(block)

	created = False
	last_score = 0
	speed_change = 18
	ball_change = 0

	while game_quit!=True:
		clock.tick(60)
		gameDisplay.blit(bg,(0,0))

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key==pygame.K_LEFT:
					player.speed=-speed_change
				if event.key==pygame.K_RIGHT:
					player.speed=speed_change
				if event.key==pygame.K_SPACE:
					if ball.space_flag !=3:
						ball.space_flag=1

		if ball.rect.y > window_height and created == False:
			death = Gameover()
			game_over_gp.add(death)
			created = True

		if (player.score % 2) == 0 and player.score!=0 and player.score>last_score:
			speed_change += 1
			ball_change += 1
			last_score = player.score
			if ball.y_speed>0:
				ball.y_speed+=1
			else:
				ball.y_speed-=1

		player_gp.update()
		ball_gp.update(player,player_gp,ball_change)
		blocks_gp.update(ball,ball_gp,player)
		game_over_gp.update(created)

		player_gp.draw(gameDisplay)
		ball_gp.draw(gameDisplay)
		blocks_gp.draw(gameDisplay)
		game_over_gp.draw(gameDisplay)

		score(player.score)
		pygame.display.flip()

gameloop()
pygame.quit()
quit()
