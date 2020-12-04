import pygame,random, time

pygame.init()
FPS = 60
clock = pygame.time.Clock()

window_width=1000
window_height=1000
gamedisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Memory game')

images1 = ['images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png']
images2 = ['images/cat1.png','images/cat2.png','images/cat1.png','images/cat2.png']
images3 = ['images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat1.png','images/cat2.png','images/cat3.png','images/cat4.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png','images/cat5.png','images/cat6.png','images/cat7.png','images/cat8.png','images/cat9.png','images/cat10.png','images/cat11.png','images/cat12.png','images/cat9.png','images/cat10.png','images/cat11.png','images/cat12.png','images/cat13.png','images/cat14.png','images/cat15.png','images/cat16.png','images/cat13.png','images/cat14.png','images/cat15.png','images/cat16.png','images/cat17.png','images/cat18.png','images/cat17.png','images/cat18.png']


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))


def menu():
	pygame.draw.rect(gamedisplay, (0,255,0), (window_width/8, (window_height/2)-75,150,150), 0)
	pygame.draw.rect(gamedisplay, (255,0,0), ((window_width/8)+300, (window_height/2)-75, 150,150), 0)
	pygame.draw.rect(gamedisplay, (255,255,0), ((window_width/8)+600, (window_height/2)-75, 150,150), 0)
	drawtext('2x2', (window_width/8)+40, (window_height/2)-25, (0,0,0), 35)
	drawtext('4x4', (window_width/8)+340, (window_height/2)-25, (0,0,0), 35)
	drawtext('6x6', (window_width/8)+640, (window_height/2)-25, (0,0,0), 35)



class Game():
	def __init__(self):
		self.opened_cards = []
		self.first_click = False
		self.start = 0
		self.end = 0
		self.last_update = 0
		self.img_to_delete = None



class Cards(pygame.sprite.Sprite):
	def __init__(self,x,y,images):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((100,100))
		self.image.fill((0,255,0))
		self.size = self.image.get_rect().size
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.card_image = random.choice(images)
		images.remove(self.card_image)
		self.size_change = 100
		self.turn = False
		self.iamclicked = False
		self.backturn = False


	def update(self,event):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		for events in event:
			if events.type == pygame.MOUSEBUTTONDOWN:
				if (mouse_x > self.rect.x) and (mouse_x < self.rect.x+self.size[0]) and (mouse_y > self.rect.y) and (mouse_y < self.rect.y+self.size[1]) and self.iamclicked==False and len(game.opened_cards)<2 and self.backturn==False:
					game.last_update = pygame.time.get_ticks()
					self.turn = True
					self.iamclicked = True
					game.opened_cards.append(self.card_image)

					if game.first_click == False:
						game.start = pygame.time.get_ticks()
						game.first_click = True


		if self.turn == True:
			if self.size_change > 1:
				self.size_change -= 4
				self.image = pygame.transform.scale(self.image,(int(self.size_change),100))
			if self.size_change<1 and self.size_change>-100:
				self.image = pygame.image.load(self.card_image)
				self.size_change -= 4
				self.image = pygame.transform.scale(self.image,(int(self.size_change)*-1,100))

		if self.backturn == True:
			if self.size_change < -4:
				self.size_change += 4
				self.image = pygame.transform.scale(self.image,(int(self.size_change)*-1,100))
			if self.size_change > -5 and self.size_change<100:
				self.size_change += 4
				self.image=pygame.Surface((100,100))
				self.image.fill((0,255,0))
				self.image = pygame.transform.scale(self.image,(int(self.size_change),100))
			if self.size_change > 96:
				self.backturn = False


		self.now = pygame.time.get_ticks()
		if len(game.opened_cards) == 2:
			game.img_to_delete = game.opened_cards[0]
			if self.now - game.last_update > 1200:
				if (game.opened_cards[0] != game.opened_cards[1]):
					for sprite in cards_gp:
						sprite.backturn = True
						sprite.iamclicked = False
						sprite.turn = False
					game.opened_cards = []
				else:
					for sprite in cards_gp:
						if sprite.card_image == game.img_to_delete:
							sprite.kill()
					game.opened_cards = []
					game.img_to_delete = None


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))


cards_gp = pygame.sprite.Group()
game = Game()
game_quit = False


def gameloop():
	timer = True
	display_menu = True
	opened_cards = []

	but_size = 150
	two_table_but_coords = (window_width/8,(window_height/2)-75,(window_width/8)+but_size,((window_height/2)-75)+but_size)
	four_table_but_coords = ((window_width/8)+300, (window_height/2)-75, ((window_width/8)+300)+but_size, ((window_height/2)-75)+but_size)
	six_table_but_coords = ((window_width/8)+600, (window_height/2)-75, ((window_width/8)+600)+but_size,((window_height/2)-75)+but_size)
	two = False
	four = False
	six = False

	try:
		with open('game_times.txt','r') as file:
			lowest_times = file.read()
			lowest_times = lowest_times.replace("[","")
			lowest_times = lowest_times.replace("]","")
			lowest_times = lowest_times.replace("'","")
			lowest_times = lowest_times.split(",")
			two_table_best_time = lowest_times[0]
			four_table_best_time = lowest_times[1]
			six_table_best_time = lowest_times[2]
	except FileNotFoundError:
		lowest_times = [10000,100000,100000]
		with open('game_times.txt','w') as file:
			file.write(str(lowest_times))
		two_table_best_time = 100000
		four_table_best_time = 100000
		six_table_best_time = 100000


	while game_quit!=True:
		gamedisplay.fill((0,0,0))
		mouse_x, mouse_y = pygame.mouse.get_pos()
		clock.tick(FPS)

		ev = pygame.event.get()
		for event in ev:
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		if display_menu == True:
			menu()
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if ((mouse_x > two_table_but_coords[0]) and (mouse_x < two_table_but_coords[2])) and ((mouse_y > two_table_but_coords[1]) and (mouse_y < two_table_but_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0]==1:
					two = True
					y=380

					for i in range(2):
						x=380
						c = 0
						while c != 2:
							card = Cards(x,y,images2)
							cards_gp.add(card)
							x += 150
							c += 1
						y += 150

					display_menu = False

			if ((mouse_x > four_table_but_coords[0]) and (mouse_x < four_table_but_coords[2])) and ((mouse_y > four_table_but_coords[1]) and (mouse_y < four_table_but_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0]==1:
					four = True
					y=220

					for i in range(4):
						x=220
						c = 0
						while c != 4:
							card = Cards(x,y,images1)
							cards_gp.add(card)
							x += 150
							c += 1
						y += 150

					display_menu = False

			if ((mouse_x > six_table_but_coords[0]) and (mouse_x < six_table_but_coords[2])) and ((mouse_y > six_table_but_coords[1]) and (mouse_y < six_table_but_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0]==1:
					six = True
					y=60

					for i in range(6):
						x=60
						c = 0
						while c != 6:
							card = Cards(x,y,images3)
							cards_gp.add(card)
							x += 150
							c += 1
						y += 150

					display_menu = False


		if len(cards_gp) == 0 and display_menu == False:
			if timer == True:
				game.end = pygame.time.get_ticks()
				timer = False

			if two == True:
				if (game.end-game.start)//1000 < int(two_table_best_time):
					lowest_times[0] = (game.end-game.start)//1000
					best_time = lowest_times[0]
					file = open('game_times.txt','w')
					file.write(str(lowest_times))
					file.close()
				else:
					best_time = two_table_best_time
				two = False

			if four == True:
				if (game.end-game.start)//1000 < int(four_table_best_time):
					lowest_times[1] = (game.end-game.start)//1000
					best_time = lowest_times[1]
					file = open('game_times.txt','w')
					file.write(str(lowest_times))
					file.close()
				else:
					best_time = four_table_best_time
				four = False

			if six == True:
				if (game.end-game.start)//1000 < int(six_table_best_time):
					lowest_times[2] = (game.end-game.start)//1000
					best_time = lowest_times[2]
					file = open('game_times.txt','w')
					file.write(str(lowest_times))
					file.close()
				else:
					best_time = six_table_best_time
				six = False


			drawtext('You have played for '+str((game.end-game.start)//1000)+' seconds',(window_width/2)-440,(window_height/2)-70,(0,255,0),60)
			drawtext('The best time for this group of games is '+str(best_time)+' seconds',(window_width/2)-440,(window_height/2)+70,(0,255,0),30)
			pygame.display.flip()
			time.sleep(5)
			exit()
		cards_gp.update(ev)
		cards_gp.draw(gamedisplay)
		pygame.display.flip()



gameloop()
pygame.quit()
