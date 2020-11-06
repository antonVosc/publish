import pygame,random

pygame.init()
FPS = 60
clock = pygame.time.Clock()

window_width=1000
window_height=1000
gamedisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Memory game') #the name of the poject (appears at the top of the game window as a name of a game)
images = ['images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png']

class Cards(pygame.sprite.Sprite):
	def __init__(self,x,y):
		global images
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((100,100))
		self.image.fill((0,255,0))
		self.size = self.image.get_rect().size
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.card_image = random.choice(images)
		images.remove(self.card_image)

	def update(self,event):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		for events in event:
			if events.type == pygame.MOUSEBUTTONDOWN:
				if (mouse_x > self.rect.x) and (mouse_x < self.rect.x+self.size[0]) and (mouse_y > self.rect.y) and (mouse_y < self.rect.y+self.size[1]):
					self.image = pygame.image.load(self.card_image)



def gameloop():
	game_quit = False

	cards_gp = pygame.sprite.Group()
	y=260

	for i in range(2):
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
		ev = pygame.event.get()
		for event in ev:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()


		gamedisplay.fill((0,0,0))
		cards_gp.update(ev)
		cards_gp.draw(gamedisplay)
		pygame.display.flip()

gameloop()
pygame.quit()
