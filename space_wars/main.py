import pygame,time
pygame.init()
window_width=1440#user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=900#user32.GetSystemMetrics(1) #getting my screen height from line 3
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('space wars') #the name of the poject (appears at the top of the game window as a name of a game)
spaceship=pygame.image.load('spaceship.png') #loading an emeny car image into a project
bg = pygame.image.load('stars.jpg')
bg = pygame.transform.scale(bg,(window_width,window_height))
bullet = pygame.image.load('bullet.png')

spaceship_size = spaceship.get_rect().size
spaceship = pygame.transform.scale(spaceship, (int(spaceship_size[0]/12),int(spaceship_size[1]/12)))
spaceship_size = spaceship.get_rect().size

bullet_size = bullet.get_rect().size
bullet = pygame.transform.scale(bullet, (int(bullet_size[0]/10),int(bullet_size[1]/10)))

blue=(0,0,255)

def draw_ship(x,y):
	gamedisplay.blit(spaceship,(x,y))

def draw_bul(x,y,vis):
	if vis == True:
		gamedisplay.blit(bullet, (x, y))

def gameloop():
	x=(window_width*0.5)-(spaceship_size[0]*0.5)
	y=window_height-spaceship_size[1]
	bullet_y=window_height-spaceship_size[1]
	game_quit = False
	bullet_vis = False
	bullet_x=0
	while game_quit!=True:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		gamedisplay.blit(bg,(0,0))
		for event in pygame.event.get(): #check every key I press
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE: ##what happens if I press Esc key
					pygame.quit() #close the game window
					quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				bullet_vis=True
				bullet_x=mouse_x+(spaceship_size[0]/2)-13
		if bullet_vis == True and bullet_y>0:
			bullet_y=bullet_y-15
		else:
			bullet_vis=False
			bullet_y=window_height-spaceship_size[1]
		draw_bul(bullet_x,bullet_y,bullet_vis)
		draw_ship(mouse_x,y)
		pygame.display.update()
gameloop()
pygame.quit()
quit()
