import pygame,ctypes, time,random #importing all the libraries needed
pygame.init() #initialising pygame to use it in the project
user32 = ctypes.windll.user32 #getting my screen dimensions (width and height)
#window_width=3840
#window_height = 2160
green=(0,255,0) #RGB values for green colour
black=(0,0,0) #RGB values for black colour
red = (255,0,0)
window_width=user32.GetSystemMetrics(0) #getting my screen width from line 3
window_height=user32.GetSystemMetrics(1) #getting my screen height from line 3
gamedisplay = pygame.display.set_mode((window_width,window_height),pygame.FULLSCREEN)#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('car game') #the name of the poject (appears at the top of the game window as a name of a game)
car_img = pygame.image.load('car.png') #loading a car image into a project
road = pygame.image.load('road.png') #loading a road image into a project
enemy_car=pygame.image.load('enemy_car.png') #loading an emeny car image into a project
road_size=road.get_rect().size #getting the dimensions of a picture of a road
enemy_size = enemy_car.get_rect().size #getting the dimensions of a picture of an enemy car
car_size = car_img.get_rect().size #getting the dimensions of a picture of my car
smallfont = pygame.font.SysFont('comicsansms',25) #setting up the correct font and size for a score

def score(score): #a function for displaying the score on the screen
	text=smallfont.render("Score: "+str(score),True, black) #set up the text with the font in black colour
	gamedisplay.blit(text,[0,0]) #showing the score on the up left side of the screen

def car(x,y): #a car display function with coordinates where it's going to appear
	gamedisplay.blit(car_img,(x,y)) #showing the car on the screen in the correct place

def road_surf(x,y): #a road display function with coordinates where it's going to appear
	gamedisplay.blit(road,(x,y)) #showing the road on the screen in the correct place

def enemy(x,y): #an enemy car display function with coordinates where it's going to appear
	gamedisplay.blit(enemy_car,(x,y)) #showing the enemy car on the screen in the correct place

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

def gameloop(): #a main function where all fumction are brought together and where the actual game is happening
	x=(window_width*0.5)-car_size[0] #x coordinate of left side of my car
	y=window_height-car_size[1] #y coordinate of left side of my car
	start_cord_list = [(window_width*0.5)+(enemy_size[0]-50),(window_width*0.5)+(enemy_size[0]+120),(window_width*0.5)-enemy_size[0]-250,(window_width*0.5)-enemy_size[0]-50] #list of all possible starting x positions of an enemy car
	enemy_x=random.choice(start_cord_list) #choose a random value from the list above so an enemy car sets of from different places each time
	enemy_y=-300 #starting y position for enemy car
	road_x=(window_width*0.5)-447 #x position of left side of the road
	start_road=-900 #y position where the road starts at the buttom (I will need it later for new layersd of the road)
	change=0 #the value I will be changing later to adjust a turn of my car
	road_y1 = 600 #y position of the end of first layer of the road (three layers needed to cover the whole screen)
	road_y2 = 700-(road_size[1]) #y position of the end of second layer of the road (three layers needed to cover the whole screen)
	road_y3 = 800-(road_size[1]*2) #y position of the end of third layer of the road (three layers needed to cover the whole screen)
	road_speed = 2 #the speed with which a road will move (the road will need to move as well to create an effect that a car moves very fast)
	my_score = 0 #the score count which will go up by 1 each time I drive past the enemy car
	car_speed_increase = 3.5 #the increase of speed of enemy car after each pass so the game gets harder
	increase_road_speed=0.5 #the increase of speed of road after each pass so the game gets harder
	speed_of_turn=2 #how sharp I am turning annd which way
	while True: #the events in this loop will always happen
			#print(road_y)
		for event in pygame.event.get(): #check every key I press
			#print(pygame.event)
			if event.type==pygame.KEYDOWN: #what happens if I press something
				if event.key==pygame.K_LEFT: #what happens if I press left key
					change=-speed_of_turn #left turn
				if event.key==pygame.K_RIGHT: #what happens if I press right key
					change=+speed_of_turn #right turn
					#message_display('Welcome to the game!')
				if event.key==pygame.K_ESCAPE: ##what happens if I press Esc key
					pygame.quit() #close the game window
					quit() #stop my game and pygame from running

		x=x+change #moving a car to the right or to the left
		gamedisplay.fill(green) #green background using RGB colour I've assigned at the beginning (line 6)
		road_y1+=road_speed #change y position of the first layer of the road which creates an effect that it moves
		road_y2+=road_speed #change y position of the second layer of the road which creates an effect that it moves
		road_y3+=road_speed #change y position of the third layer of the road which creates an effect that it moves
		enemy_y=enemy_y+car_speed_increase #make the enemy car move faster to make the game harder
		if road_y1 > window_height: #if the first layer of the road reached the end
			road_y1 = start_road #move it back to the top of the screen
		if road_y2 > window_height: #if the second layer of the road reached the end
			road_y2 = start_road #move it back to the top of the screen
		if road_y3 > window_height: #if the first layer of the road reached the end
			road_y3 = start_road #move it back to the top of the screen
		if y<enemy_y+enemy_size[1] and x<enemy_x+enemy_size[0] and not enemy_x> x+car_size[0]: #if the left of my car touched the right of enemy car and another way around
			crash(my_score) #display the 'crashed' message on the screen
		if y<enemy_y-enemy_size[1]: #if top of my car is less than left of enemy car (if I didn't crash)
			if my_score % 3 == 0 and my_score!=0: #each three points
				speed_of_turn=speed_of_turn+1 #make the turn a bit sharper
			my_score=my_score+1 #increasing the score
			enemy_x=random.choice(start_cord_list) #move the enemy car back to the top of the screen (x)
			enemy_y=random.randint(-600,-300) #move the enemy car back to the top of the screen (y)
			car_speed_increase = car_speed_increase + 0.6*my_score #make my car move faster as I increase the points to make the game harder
			road_speed=road_speed+0.4*my_score #make the road move faster as well as I increase the points to make the game even more harder


		road_surf((window_width/2)-(road_size[0]/2),road_y1) #creating a new layer of the road
		road_surf((window_width/2)-(road_size[0]/2),road_y2) #creating a new layer of the road
		road_surf((window_width/2)-(road_size[0]/2),road_y3) #creating a new layer of the road

		if x<road_x or x>road_x+road_size[0]-car_size[0]: #if the car touched left or right side of the road
			crash(my_score) #display the 'crashed' message on the screen
		enemy(enemy_x,enemy_y) #call enemy function to display an enemy car on to a screen
		car(x,y) #call car function to display an my car on to a screen
		score(my_score) #call score function to count my score
		pygame.display.update() #update the screen to see all the changes and all animation

gameloop() #call the main function to start the game
pygame.quit() #exit pygame at the end
