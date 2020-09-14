import pygame,ctypes,random,sys
from PyQt5 import QtCore, QtGui, QtWidgets

#Init
pygame.init()
FPS = 60
clock = pygame.time.Clock()
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0)
window_height=user32.GetSystemMetrics(1)
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)
pygame.display.set_caption('Car Race')
obsticles = ['images/cone.png','images/road-closed.png','images/lives.png']

white = (255,255,255)

class Player(pygame.sprite.Sprite):
	def __init__(self,lives):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/car.png') #loading an emeny car image into a project
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.y = window_height-self.size[1]
		self.lives = lives
		self.score = 0

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]

class Obsticles(pygame.sprite.Sprite):
	def __init__(self,speed,img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('{}'.format(img))
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,window_width-self.size[0])
		self.rect.y = self.size[1] * -1
		self.speed = speed

	def update(self):
		self.rect.y += self.speed
		if self.rect.y > window_height:
			player.score += 1
			self.kill()


def drawtext(text, x, y, color, size):
	myfont = pygame.font.SysFont('Comic Sans MS', size)
	textsurface = myfont.render(text,False, color)
	gamedisplay.blit(textsurface,(x, y))


def menu():
	pygame.draw.rect(gamedisplay, (0,255,0), (window_width/8, window_height/4,300,300), 0)
	pygame.draw.rect(gamedisplay, (255,255,0), ((window_width/2)-150, window_height/4, 300, 300), 0)
	pygame.draw.rect(gamedisplay, (255,0,0), ((window_width/8)*6, window_height/4, 300, 300), 0)
	drawtext('Play', (window_width/8)+90, (window_height/4)+90, (0,0,0), 70)
	drawtext('Stats', (window_width/2)-100, (window_height/4)+90, (0,0,0), 70)
	drawtext('Exit', ((window_width/8)*6)+85, (window_height/4)+90, (0,0,0), 70)

def get_highest_score():
	with open('scores.txt', 'r') as f:
		all_scores = f.read()
	f.close()
	if all_scores == "":
		all_scores =0
	return all_scores

def gameloop():
	global obsticles_gp,player,speed

	game_quit = False
	speed = 5
	lives = 3

	player_gp = pygame.sprite.Group()
	player = Player(lives)
	player_gp.add(player)

	obsticles_gp = pygame.sprite.Group()

	live_gp = pygame.sprite.Group()

	but_size = 300
	start_but_coords = (window_width/8,window_height/4,(window_width/8)+but_size,(window_height/4)+but_size)
	stats_but_coords = ((window_width/2)-150,window_height/4,((window_width/2)-150)+but_size,(window_height/4)+but_size)
	ext_btn_coords = ((window_width/8)*6,window_height/4,((window_width/8)*6)+but_size,(window_height/4)+but_size)
	ext_stats_btn_coors = ((window_width/8)*6.6,(window_height/2)+600,((window_width/8)*6.6)+400,(window_height/2)+700)
	start_game = False
	display_menu = True
	stats = False
	high_score = True
	score_from_file = get_highest_score()

	while game_quit!=True:
		clock.tick(FPS)
		gamedisplay.fill(white)

		#Event handling
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()

		if display_menu == True:
			menu()
		else:
			player_gp.draw(gamedisplay)
			player_gp.update()
			obsticles_gp.draw(gamedisplay)
			obsticles_gp.update()
			live_gp.draw(gamedisplay)
			live_gp.update()
			drawtext('Lives: '+str(lives), 0,0, (0,0,0), 70)
			drawtext('Score: '+str(player.score), window_width-350,0, (0,0,0), 70)

		if stats == True:
			gamedisplay.fill(white)
			if high_score == True:
				high_score = False
			drawtext('High score: '+score_from_file, (window_width/2)-225,(window_height/2)-100, (0,0,0), 70)
			pygame.draw.rect(gamedisplay, (0,0,255), ((window_width/8)*6.6, (window_height/2)+600, 400, 100), 0)
			drawtext('Exit', (window_width/8)*7, (window_height/2)+600, (0,0,0), 70)
			if ((mouse_x > ext_stats_btn_coors[0]) and (mouse_x < ext_stats_btn_coors[2])) and ((mouse_y > ext_stats_btn_coors[1]) and (mouse_y < ext_stats_btn_coors[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0]==1:
					gamedisplay.fill(white)
					stats = False
					menu()


		prob = random.randint(0,1000)
		if prob <= 20: #2%
			obst = Obsticles(speed,obsticles[0])
			obsticles_gp.add(obst)
			if prob <= 4: #2%
				obst = Obsticles(speed,obsticles[1])
				obsticles_gp.add(obst)
			if prob <= 2:
				obst = Obsticles(speed,obsticles[2])
				live_gp.add(obst)

		collision = pygame.sprite.groupcollide(player_gp,obsticles_gp,False,True)
		collision2 = pygame.sprite.groupcollide(player_gp,live_gp,False,True)

		if collision and prob > 2:
			lives -= 1

		if collision2:
			lives += 1

		if lives == 0:
			if player.score > int(score_from_file):
				with open('scores.txt', 'w') as f:
					f.write(str(player.score))
					f.close()
			pygame.quit()
			quit()

		speed += 0.005
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if ((mouse_x > start_but_coords[0]) and (mouse_x < start_but_coords[2])) and ((mouse_y > start_but_coords[1]) and (mouse_y < start_but_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0]==1:
				display_menu = False



		if ((mouse_x > ext_btn_coords[0]) and (mouse_x < ext_btn_coords[2])) and ((mouse_y > ext_btn_coords[1]) and (mouse_y < +ext_btn_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0] == 1:
				pygame.quit()
				quit()

		if ((mouse_x > stats_but_coords[0]) and (mouse_x < stats_but_coords[2])) and ((mouse_y > stats_but_coords[1]) and (mouse_y < stats_but_coords[3])):
			pres = pygame.mouse.get_pressed()
			if pres[0]==1:
				stats=True
		pygame.display.flip()



gameloop()
pygame.quit()
quit()
