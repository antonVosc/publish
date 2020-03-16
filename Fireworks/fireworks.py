import pygame,random
pygame.init()

FPS = 100
clock = pygame.time.Clock()
window_width=1000
window_height=1000
gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Fireworks')

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((20,20))
		self.image.fill((0,0,0))
		pygame.draw.circle(self.image,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(10,10),10,0)
		self.rect=self.image.get_rect()
		self.rect.x, self.rect.y=pygame.mouse.get_pos()
		self.x_speed, self.y_speed = random.randint(-15,15), random.randint(-15,15)
		self.gravity = 0.7

	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		self.y_speed += self.gravity
		if self.rect.y>window_height:
			self.kill()


def gameloop():
	game_quit = False
	ball_gp = pygame.sprite.Group()

	while game_quit!=True:
		clock.tick(FPS)
		gameDisplay.fill((0,0,0))

		mouse_click = pygame.mouse.get_pressed()
		if mouse_click[0]>0:
			for i in range(3):
				ball=Ball()
				ball_gp.add(ball)

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		ball_gp.update()
		ball_gp.draw(gameDisplay)
		pygame.display.flip()

gameloop()
pygame.quit()
quit()
