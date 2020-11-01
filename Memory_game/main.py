import pygame

pygame.init()
FPS = 60
clock = pygame.time.Clock()

window_width=1000
window_height=1000
gamedisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Memory game') #the name of the poject (appears at the top of the game window as a name of a game)

class Cards(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((100,100))
		self.image.fill((0,255,0))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

def gameloop():
	game_quit = False

	cards_gp = pygame.sprite.Group()
	y=260

	for i in range(3):
		x=240
		c = 0
		while c != 4:
			card = Cards(x,y)
			cards_gp.add(card)
			x += 150
			c += 1
		y += 150


	while game_quit!=True:
		clock.tick(FPS)
		gamedisplay.fill((0,0,0))

		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		cards_gp.update()
		cards_gp.draw(gamedisplay)
		pygame.display.flip()

gameloop()
pygame.quit()
