import pygame,ctypes,random,time,sys
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
car_states = ['images/car.png','images/car_crashed.png']

white = (255,255,255)

class Player(pygame.sprite.Sprite):
	def __init__(self,lives):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(car_states[0])
		self.size = self.image.get_rect().size
		self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
		self.size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.y = window_height-self.size[1]
		self.lives = lives
		self.score = 0
		self.is_crashed = False
		self.max_prob = 1000

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]
		if self.rect.x < 0:
			self.rect.x = 0
		if (self.rect.x+self.size[0]) > window_width:
			self.rect.x = window_width-self.size[0]
		if self.is_crashed == True:
			self.image=pygame.image.load(car_states[1])
			self.image = pygame.transform.scale(self.image,(int(self.size[0]),int(self.size[1])))
		else:
			self.image=pygame.image.load(car_states[0])
			self.image = pygame.transform.scale(self.image,(int(self.size[0]),int(self.size[1])))


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
		if (self.rect.y > window_height) and (self.image != obsticles[2]):
			player.score += 1
			if player.max_prob<500:
				player.max_prob = 500
			else:
				player.max_prob -= 50
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
	try:
		with open('scores.txt', 'r') as f:
			all_scores = f.read()
			if all_scores == "":
				all_scores = 0
	except FileNotFoundError:
		with open('scores.txt', 'w') as f:
			all_scores = 0
	f.close()
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
	milisecs = 0
	start_but_coords = (window_width/8,window_height/4,(window_width/8)+but_size,(window_height/4)+but_size)#left,top,right,bot
	stats_but_coords = ((window_width/2)-150,window_height/4,((window_width/2)-150)+but_size,(window_height/4)+but_size)
	ext_btn_coords = ((window_width/8)*6,window_height/4,((window_width/8)*6)+but_size,(window_height/4)+but_size)
	ext_stats_btn_coords = ((window_width/8)*6.6,(window_height/2)+600,((window_width/8)*6.6)+400,(window_height/2)+700)
	play_again_btn_coords = ((window_width/2)-400,window_height-400,((window_width/2)-400)+but_size,(window_height-400)+but_size)
	exit_after_game_btn_coords = ((window_width/2)+100,window_height-400,(window_width+100)+but_size,(window_height-400)+but_size)
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
			if ((mouse_x > ext_stats_btn_coords[0]) and (mouse_x < ext_stats_btn_coords[2])) and ((mouse_y > ext_stats_btn_coords[1]) and (mouse_y < ext_stats_btn_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0]==1:
					gamedisplay.fill(white)
					stats = False
					menu()

		prob = random.randint(0,player.max_prob)
		if prob <= 80 and lives > 0 and display_menu == False: #2%
			obst = Obsticles(speed,obsticles[0])
			obsticles_gp.add(obst)
			if prob <= 16: #2%
				obst = Obsticles(speed,obsticles[1])
				obsticles_gp.add(obst)
			if prob <= 8:
				obst = Obsticles(speed,obsticles[2])
				live_gp.add(obst)

		collision = pygame.sprite.groupcollide(player_gp,obsticles_gp,False,True)
		collision2 = pygame.sprite.groupcollide(player_gp,live_gp,False,True)
		mouse_x, mouse_y = pygame.mouse.get_pos()

		if collision and prob > 2:
			lives -= 1
			player.is_crashed = True
			milisecs = pygame.time.get_ticks()

		now = pygame.time.get_ticks()
		if player.is_crashed == True:
			if now > milisecs + 2000:
				player.is_crashed = False

		if collision2:
			lives += 1

		if lives == 0:
			if player.score > int(score_from_file):
				score_from_file = player.score
				with open('scores.txt', 'w') as f:
					f.write(str(player.score))
				f.close()
			gamedisplay.fill(white)
			drawtext('Game Over!', (window_width/8)*3.5, (window_height/2)-100, (0,0,0), 70)
			drawtext('Your score is '+str(player.score), (window_width/8)*3.3, (window_height/2)-10, (0,0,0), 70)
			drawtext('Your highest score is '+str(score_from_file), ((window_width/8)*3.3)-150, (window_height/2)+80, (0,0,0), 70)
			pygame.draw.rect(gamedisplay, (0,0,255), ((window_width/2)-400, window_height-400, 300, 300), 0)
			drawtext('Main menu', (window_width/2)-395, window_height-300, (0,0,0), 60)
			pygame.draw.rect(gamedisplay, (255,0,0), ((window_width/2)+100, window_height-400, 300, 300), 0)
			drawtext('Exit', (window_width/2)+200, window_height-300, (0,0,0), 60)
			player.kill()
			for obst in obsticles_gp:
				obst.kill()
			for obst in live_gp:
				obst.kill()
			if ((mouse_x > exit_after_game_btn_coords[0]) and (mouse_x < exit_after_game_btn_coords[2])) and ((mouse_y > exit_after_game_btn_coords[1]) and (mouse_y < exit_after_game_btn_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0] == 1:
					pygame.quit()
					quit()
			if ((mouse_x > play_again_btn_coords[0]) and (mouse_x < play_again_btn_coords[2])) and ((mouse_y > play_again_btn_coords[1]) and (mouse_y < play_again_btn_coords[3])):
				pres = pygame.mouse.get_pressed()
				if pres[0] == 1:
					gameloop()
			pygame.display.flip()

		speed += 0.005

		if display_menu == True:
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
