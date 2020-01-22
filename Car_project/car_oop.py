import pygame, time,random,ctypes #importing all the libraries needed
pygame.init() #initialising pygame to use it in the project
FPS = 60
clock = pygame.time.Clock()

green=(0,255,0) #RGB values for green colour
black=(0,0,0) #RGB values for black colour
red = (255,0,0)
user32 = ctypes.windll.user32
window_width=user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=user32.GetSystemMetrics(1) #getting my screen height from line 3
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('car game') #the name of the poject (appears at the top of the game window as a name of a game)
smallfont = pygame.font.SysFont('comicsansms',75) #setting up the correct font and size for a score

bg = pygame.image.load('images/grass.jpg')
bg = pygame.transform.scale(bg,(window_width,window_height))


def score(score): #a function for displaying the score on the screen
	text=smallfont.render("Score: "+str(score),True, red) #set up the text with the font in black colour
	gamedisplay.blit(text,[0,0]) #showing the  on the up left side of the screen


def text_object(text,font): #a function for setting up the text with the correct font
	text_surface = font.render(text,True,red) #setting up the text font and colour (black)
	return text_surface,text_surface.get_rect() #returning all the variables used in this function to use them in other places of the project

def message_display(text): #a function for showing the message on the sceen when I've crashed
	message = pygame.font.Font('freesansbold.ttf',150) #setting up the correct font and size for a message
	text_surf,text_rect = text_object(text,message) #adjusting text settings
	text_rect.center = ((window_width/2,window_height/2)) #where the text will appear with the function is called
	gamedisplay.blit(text_surf,text_rect) #show the text on the screen with the correct settings and in the correct place on the screen
	pygame.display.update() #change the screen to see the text
	time.sleep(5) #wait 5 seconds and don't do anything for the player to read the text

def crash(my_score):
	parse_message = 'crashed. Your score is '+str(my_score)
	message_display(parse_message) #display the 'crashed' message on the screen
	time.sleep(5)
	gameloop()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/car.png') #loading a car image into a project
		self.car_size = self.image.get_rect().size #getting the dimensions of a picture of my car
		self.rect = self.image.get_rect()
		self.rect.x=(window_width*0.5)-self.car_size[0] #x coordinate of left side of my car
		self.rect.y=window_height-self.car_size[1]
		self.x_speed = 0
		self.score = 0

	def update(self,enemy):
		self.rect.x+=self.x_speed


class Road(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load('images/road.png')
		self.road_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = (window_width*0.5)-(self.road_size[0]*0.5)
		self.rect.y = window_height-(self.road_size[1]*self.position)
		self.speed=2

	def update(self):
		if self.rect.y>window_height:
				self.rect.y = 0 - self.road_size[1]
		self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
	def __init__(self,speed,road):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/enemy_car.png')
		self.enemy_size = self.image.get_rect().size
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(road.rect.x+70,road.rect.x+road.road_size[0]-self.enemy_size[0]-70)#(window_width*0.5)-self.enemy_size[0]
		self.rect.y=0-self.enemy_size[1]-random.randint(50,700)
		self.speed=speed

	def update(self, player):
		self.rect.y += self.speed


def gameloop():
	#game speed increse
	car_speed_increase = 3.5
	increase_road_speed=0.5
	turn = 5
	speed=10
	clock.tick(FPS)

	player_gp = pygame.sprite.Group()
	road_gp = pygame.sprite.Group()
	enemy_gp = pygame.sprite.Group()

	player=Player()
	player_gp.add(player)

	for i in range(1,5):
		road = Road(i)
		road_gp.add(road)

	enemy=Enemy(speed,road)
	enemy_gp.add(enemy)

	game_quit=False
	while game_quit!=True:
		gamedisplay.blit(bg,(0,0))
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key==pygame.K_LEFT:
					player.x_speed=-turn
				if event.key==pygame.K_RIGHT:
					player.x_speed=turn

		if player.rect.x<road.rect.x or player.rect.x+player.car_size[0]>road.rect.x+road.road_size[0]:
			crash(player.score)

		if  window_height<enemy.rect.y-enemy.enemy_size[1]:
				speed=speed+5
				player.score+=1
				turn=turn+2
				enemy.kill()
				enemy=Enemy(speed,road)
				enemy_gp.add(enemy)

		crashed = pygame.sprite.groupcollide(player_gp,enemy_gp,True,True)
		if crashed:
			crash(player.score)
			game_quit=True

		road_gp.update()
		player_gp.update(enemy)
		enemy_gp.update(player)

		road_gp.draw(gamedisplay)
		player_gp.draw(gamedisplay)
		enemy_gp.draw(gamedisplay)

		score(player.score)
		pygame.display.flip()

gameloop()
pygame.quit()
