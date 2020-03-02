import pygame,time,random,ctypes

#Init
pygame.init()
FPS = 100

clock = pygame.time.Clock()
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=user32.GetSystemMetrics(1) #getting my screen height from line
gameDisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Ping pong') #the name of the poject (appears at the top of the game window as a name of a game)

bg = pygame.image.load('images/background.png')
bg = pygame.transform.scale(bg,(window_width,window_height))

smallfont = pygame.font.SysFont('comicsansms',75) #setting up the correct font and size for a score

white = (255,255,255)
red = (255,0,0)

def score(score,x,y): #a function for displaying the score on the screen
	score=smallfont.render("Score: "+str(score),True, white) #set up the text with the font in black colour
	gameDisplay.blit(score,[x,y]) #showing the  on the up left side of the screen


class Player(pygame.sprite.Sprite):
	def __init__(self,num):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/{}.png'.format(num))
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]*1.3),int(self.size[1]*1.3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		if num == 1:
			self.rect.x = 0
		else:
			self.rect.x = window_width-self.size[0]
		self.rect.y = (window_height/2)-(self.size[1]/2)
		self.p_x_l = self.rect.x
		self.p_x_r = self.rect.x + self.size[0]
		self.score = 0
		self.speed = 10

class Ball(pygame.sprite.Sprite):
	def __init__(self,speed_up):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/ball.png')
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/10),int(self.size[1]/10)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = window_width/2
		self.rect.y = window_height/2
		self.x_speed = random.choice([random.randint(-15,-6),random.randint(6,15)])+speed_up
		self.y_speed = random.choice([random.randint(-15,-6),random.randint(6,15)])+speed_up
		self.left = 0
		self.right = 0
		self.top = 0
		self.bottom = 0
		self.touched = False

	def update(self,player1,player2,player_gp):
		self.rect.x -= self.x_speed
		self.rect.y -= self.y_speed
		self.top = self.rect.y
		self.bottom = self.rect.y+self.size[1]
		self.left = self.rect.x
		self.right = self.rect.x+self.size[0]
		if self.top<0 or self.bottom>window_height:
			self.y_speed = self.y_speed * -1
		collide = pygame.sprite.spritecollide(self,player_gp,False)
		if collide:
			self.x_speed = self.x_speed * -1
			self.touched = True
		#каждые 2 очка в сумме шарик на 2 платформа на 1
		if self.left < (window_width*0.5) and self.touched == False:
			player1.rect.y=self.rect.y-(player1.size[1]/2)
		if self.right>(window_width*0.5)+50:
			self.touched = False

		if self.right>window_width:
			player1.score += 1
			self.kill()
			ball = Ball(speed_up)
			ball_gp.add(ball)
		if self.left<0:
			player2.score += 1
			self.kill()
			ball = Ball(speed_up)
			ball_gp.add(ball)


def gameloop():
	global ball_gp,speed_up

	speed_up = 0
	game_quit = False
	clock.tick(FPS)

	player_gp = pygame.sprite.Group()
	ball_gp = pygame.sprite.Group()

	player1 = Player(1)
	player_gp.add(player1)

	player2 = Player(2)
	player_gp.add(player2)

	ball = Ball(speed_up)
	ball_gp.add(ball)

	score_changed = False

	prev_score = 0

	while game_quit!=True:
		clock.tick(60)
		gameDisplay.blit(bg,(0,0))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			player2.rect.y-=player2.speed

		if keys[pygame.K_DOWN]:
			player2.rect.y+=player2.speed


#	if keys[pygame.K_w]:
#			player1.rect.y-=player1.speed

#		if keys[pygame.K_s]:
#			player1.rect.y+=player1.speed

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		if (player1.score+player2.score) % 2 and (player1.score+player2.score)!=0 and prev_score<player1.score+player2.score:
			speed_up += 2
			player1.speed += 1
			player2.speed += 1
			prev_score=player1.score+player2.score

		player_gp.update()
		player_gp.draw(gameDisplay)

		ball_gp.update(player1,player2,player_gp)
		ball_gp.draw(gameDisplay)

		score(player1.score,0,0)
		score(player2.score,window_width-350,0)

		pygame.display.flip()

gameloop()
pygame.quit()
quit()
