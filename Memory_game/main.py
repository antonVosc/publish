import pygame,random, time

pygame.init()
FPS = 60
clock = pygame.time.Clock()

window_width=1000
window_height=1000
gamedisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Memory game') #the name of the poject (appears at the top of the game window as a name of a game)
images = ['images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png']

class Game(pygame.sprite.Sprite):
	def __init__(self):
		global images
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((1,1))
		self.image.fill((0,0,0))
		self.rect=self.image.get_rect()
		self.rect.x = 1
		self.rect.y = 1
		self.opened_cards = []
		self.deletion_count = 0
		self.first_click = False
		self.start = 0
		self.end = 0



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
					if game.first_click == False:
						game.start = pygame.time.get_ticks()
						game.first_click = True
					if len(game.opened_cards)>2:
						game.opened_cards = []
					if len(game.opened_cards)<2:
						game.opened_cards.append(self.card_image)
						self.image = pygame.image.load(self.card_image)
						gamedisplay.fill((0,0,0))
						cards_gp.draw(gamedisplay)
						pygame.display.flip()
						time.sleep(0.5)


		if len(game.opened_cards) == 2:
			if (game.opened_cards[0] != game.opened_cards[1]):
				for sprite in cards_gp:
					sprite.image = pygame.Surface((100,100))
					sprite.image.fill((0,255,0))
				game.opened_cards = []
			else:
				if self.card_image == game.opened_cards[0]:
					self.kill()
					game.deletion_count+=1
				if game.deletion_count==2:
					game.opened_cards = []
					game.deletion_count=0


cards_gp = pygame.sprite.Group()
game = Game()


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))

def clear_table():
	for card in cards_gp:
		card.kill()

def gameloop():
	game_quit = False
	timer = True

	opened_cards = []
	y=220

	for i in range(4):
		x=220
		c = 0
		while c != 4:
			card = Cards(x,y)
			cards_gp.add(card)
			x += 150
			c += 1
		y += 150

	with open('game_times.txt','r') as file:
		lowest_time = int(file.readline())
		print(lowest_time)


	while game_quit!=True:
		gamedisplay.fill((0,0,0))
		clock.tick(FPS)
		ev = pygame.event.get()
		for event in ev:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key==pygame.K_a:
					clear_table()

		if len(cards_gp) == 0:
			if timer == True:
				game.end = pygame.time.get_ticks()
				timer = False
			if (game.end-game.start)//1000 < lowest_time:
				with open('game_times.txt','w') as file:
					file.write(str((game.end-game.start)//1000))
			drawtext('You have played for '+str((game.end-game.start)//1000)+' seconds',(window_width/2)-440,(window_height/2)-70,(0,255,0),60)
			drawtext('The best time is '+str(lowest_time)+' seconds',(window_width/2)-440,(window_height/2)+70,(0,255,0),60)
			pygame.display.flip()
			time.sleep(5)
			exit()
		cards_gp.update(ev)
		cards_gp.draw(gamedisplay)
		pygame.display.flip()

gameloop()
pygame.quit()
