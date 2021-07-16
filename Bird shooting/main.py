import pygame,random

pygame.init()
FPS = 60

clock = pygame.time.Clock()
window_width=1200 #getting my screen width from line 3
window_height=1000 #getting my screen height from line
gameDisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Bird Shooting') #the name of the poject (appears at the top of the game window as a name of a game)

bg = pygame.image.load('images/bg.png')
bg = pygame.transform.scale(bg,(window_width,window_height))

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/cloud/cloud_{}.png'.format(random.randint(1,4)))
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.center = ((window_width / 2) - (self.size[0] / 2), window_height - self.size[1])
        self.rect.x = -1 * self.size[0]
        self.rect.y = random.randint(0,(window_height/2)+100)
        self.futureX = self.rect.centerx

    def update(self):
        self.futureX += 0.22
        self.rect.centerx = self.futureX
        if self.rect.x > window_width:
            self.kill()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/birds/bird_1.png')
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.center = (-1*self.size[0], random.randint(self.size[1]/2,(window_height/2)+(self.size[1]/2)))
        self.counter = 1
        self.futureX = self.rect.centerx
        self.start_time = pygame.time.get_ticks()
        self.direction = 1
        self.endpoint = random.randint(100,window_width)
        self.delta = 0.7

    def update(self):
        self.new_time = pygame.time.get_ticks()
        self.futureX += self.delta
        self.rect.centerx = self.futureX
        if (self.new_time - self.start_time) > 50:
            self.start_time = self.new_time
            self.image = pygame.image.load('images/birds/bird_{}.png'.format(self.counter))
            if self.delta<0:
                self.image = pygame.transform.flip(self.image, True, False)
            self.counter += 1
        if self.rect.centerx > window_width:
            self.kill()
        if self.counter > 15:
            self.counter = 1
        if self.rect.centerx > self.endpoint:
            self.delta = -1 * self.delta

class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/cannon/cannon_00.png')
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 450
        self.angle = 50
        self.changed_angle = False
        self.dire = 1

    def update(self):
        if self.changed_angle == True:
            self.angle += 5 * self.dire
            self.changed_angle = False
        else:
            self.image = pygame.image.load('images/cannon/cannon_00.png')
        self.old_centr = self.rect.center
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.old_centr

def gameloop():
    cloud_gp = pygame.sprite.Group()
    birds_gp = pygame.sprite.Group()
    cannon_gp = pygame.sprite.Group()

    cannon = Cannon()
    cannon_gp.add(cannon)

    while True:
        clock.tick(60)
        gameDisplay.blit(bg,(0,0))
        timer = random.randint(0, 1250)

        if timer < 2:
            cloud = Clouds()
            cloud_gp.add(cloud)

        if timer > 3 and timer < 8:
            bird = Bird()
            birds_gp.add(bird)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_LEFT:
                    cannon.changed_angle = True
                    cannon.dire = 1
                if event.key==pygame.K_RIGHT:
                    cannon.changed_angle = True
                    cannon.dire = -1

        cloud_gp.update()
        birds_gp.update()
        cannon_gp.update()

        cloud_gp.draw(gameDisplay)
        birds_gp.draw(gameDisplay)
        cannon_gp.draw(gameDisplay)

        pygame.display.flip()

gameloop()
pygame.quit()
quit()
