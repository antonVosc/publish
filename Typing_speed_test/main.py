import pygame,ctypes,random
from difflib import SequenceMatcher

pygame.init()
user32 = ctypes.windll.user32
window_width=int(user32.GetSystemMetrics(0)/2.5)
window_height=int(user32.GetSystemMetrics(1)/2.5)
gamedisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Typing test')
red = (255,0,0)
green = (0,255,0)
black=(0,0,0)


def display_text(text,size,coords,color):
	smallfont = pygame.font.SysFont('comicsansms',size)
	text=smallfont.render(text,True, color)
	gamedisplay.blit(text,coords)


def get_text():
	global ran_phrase
	text ='The government said almost half a million of the new rapid swab tests, called LamPORE, will be available from next week in adult care settings and laboratories, with millions more due to be rolled out later in the year. Additionally, thousands of DNA test machines, which have already been used in eight London hospitals and can analyse nose swabs, will be rolled out across NHS hospitals from September. Around 5,000 machines will provide 5.8 million tests in the coming months, the Department for Health said. There is currently no publicly available data on the accuracy of the new tests. But Sir John Bell, Regius Professor of Medicine at Oxford University, who has been advising the government on tests, said they produced the same "sensitivity" as the current lab-based tests.'
	words = text.split(' ')
	num_words = random.randint(8,13)
	ran_phrase = ''
	for i in range(num_words):
		word = random.choice(words)
		ran_phrase += word
		if i != num_words-1:
			ran_phrase += ' '
	return ran_phrase


phrase = get_text()
text = pygame.font.SysFont('comicsansms',32)
usr_text = ''
total = 0
correct = 0
wrong = 0


def text_check(text,user_text):
	return (SequenceMatcher(None,text,user_text).ratio())*100


def wpm(user_text):
	words = 0
	for i in range(len(usr_text)):
		if usr_text[i] == ' ' or i==len(usr_text)-1:
			words +=1
	return words


game = True
first_type = False
finish_typing = False


def new_game():
	global usr_text, phrase, first_type, finish_typing
	usr_text = ''
	phrase = get_text()
	first_type = False
	finish_typing = False


while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			quit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				pygame.quit()
				quit()
			if event.unicode.isalpha():
				usr_text += event.unicode
			if event.key == pygame.K_SPACE:
				usr_text += ' '
			if event.key == pygame.K_PERIOD:
				usr_text += '.'
			if event.key == pygame.K_COMMA:
				usr_text += ','
			if event.key == pygame.K_QUOTE:
				usr_text += '"'
			if event.key == pygame.K_5:
				usr_text += '5'
			if event.key == pygame.K_8:
				usr_text += '8'
			if event.key == pygame.K_0:
				usr_text += '0'
			if event.key == pygame.K_RETURN and len(usr_text) >= len(phrase):
				new_game()

	if len(usr_text) > 0 and first_type == False:
		first_type_milisecs = pygame.time.get_ticks()
		first_type = True
	gamedisplay.fill(black)
	if len(usr_text) >= len(phrase):
		if finish_typing == False:
			speed = wpm(usr_text)
			finish_type_milisecs = pygame.time.get_ticks()
			finish_typing = True
		seconds = (finish_type_milisecs-first_type_milisecs) // 1000
		wps = seconds / speed
		words_per_minute =  60 // wps
		final = str(round(text_check(phrase,usr_text),2))
		display_text('You wrote the phrase in '+str(seconds)+' seconds',20,[(window_width/13)+300,500],red)
		display_text('Your accuracy is '+final+' %',20,[(window_width/13)+700,500],red)
		display_text('Speed: '+str(int(words_per_minute))+' words per minute',20,[(window_width/30),500],red)
	display_text(usr_text,20,[(window_width/13)+15,300],green)
	pygame.draw.rect(gamedisplay,red,(window_width/13,195,900,50),3)
	pygame.draw.rect(gamedisplay,red,(window_width/13,290,900,50),3)
	display_text("Typing speed test",75,[window_width/5,0],red)
	display_text(phrase,20,[(window_width/13)+15,200],green)
	pygame.display.update()
