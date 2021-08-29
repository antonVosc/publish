import pygame,random,time

pygame.init()
FPS = 60

clock = pygame.time.Clock()
window_width=1200 #getting my screen width from line 3
window_height=800 #getting my screen height from line
gameDisplay = pygame.display.set_mode((window_width,window_height))#pygame.FULLSCREEN #show display with the dimensions set
pygame.display.set_caption('Bird Shooting') #the name of the poject (appears at the top of the game window as a name of a game)

bg = pygame.image.load('images/bg.png')
bg = pygame.transform.scale(bg,(window_width,window_height))
cannon_anime = ['images/cannon/cannon_00.png','images/cannon/cannon_01.png','images/cannon/cannon_02.png','images/cannon/cannon_03.png','images/cannon/cannon_04.png','images/cannon/cannon_05.png','images/cannon/cannon_06.png','images/cannon/cannon_07.png','images/cannon/cannon_08.png','images/cannon/cannon_09.png','images/cannon/cannon_010.png']


def draw_text(text, x, y, color, size):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, False, color)
    gameDisplay.blit(textsurface,(x, y))

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

class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(cannon_anime[0])
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x = window_width - self.size[0] + 70
        self.rect.y = window_height - self.size[1] - 175
        self.frame = 0
        self.last_updated = pygame.time.get_ticks()
        self.anim_fps = 60
        self.angle = 5
        self.changed_angle = False
        self.dire = 1
        self.score = 0
        self.shoot = False
        self.bullets_left = 10

    def update(self):
        last_updated = pygame.time.get_ticks()
        if self.shoot == True:
            self.last_updated = last_updated
            self.frame += 1
            if self.last_updated-last_updated > 2000:
                if self.frame == len(cannon_anime):
                    self.shoot = False
                    self.frame = 0
                else:
                    center = self.rect.center
                    self.image = pygame.image.load(cannon_anime[self.frame])
                    self.image = pygame.transform.rotate(self.image, self.angle)
                    self.rect = self.image.get_rect()
                    self.rect.center = center

        elif self.changed_angle == True:
            if self.angle>=5 and self.angle<=25:
                self.angle += 5 * self.dire
                self.changed_angle = False
            else:
                if self.angle == 0:
                    self.angle = 5
                elif self.angle == 30:
                    self.angle = 25
        else:
            self.image = pygame.image.load('images/cannon/cannon_00.png')
            self.old_centr = self.rect.center
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = self.old_centr


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/birds/bird_1.png')
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.center = (-1*self.size[0], random.randint(self.size[1]/2,(window_height/2)+(self.size[1]/2)))
        self.counter = 1
        self.futureX = self.rect.centerx
        self.space_pressed_time = pygame.time.get_ticks()
        self.direction = 1
        self.endpoint = random.randint(100,window_width)
        self.delta = 3

    def update(self,ball_gp):
        self.new_time = pygame.time.get_ticks()
        self.futureX += self.delta
        self.rect.centerx = self.futureX
        if (self.new_time - self.space_pressed_time) > 50:
            self.space_pressed_time = self.new_time
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

        death = pygame.sprite.spritecollide(self,ball_gp,False)
        if death:
            explosion = Shoot(self.rect.x,self.rect.y,self.size)
            explosion_gp.add(explosion)
            pygame.mixer.music.load('Sounds/splat.mp3')
            pygame.mixer.music.play()
            cannon.score += 1
            cannon.bullets_left += random.randint(1,3)
            self.kill()


class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ball.png')
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.1), int(self.size[1]*0.1)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_power = 0
        self.y_power = 0
        self.angle = angle

    def update(self):
        self.y_power -= 1
        self.rect.y -= self.y_power
        self.rect.x -= self.angle
        if self.rect.y > window_width or self.rect.x<0:
            self.kill()
        if self.angle < 0:
            self.x_power = self.angle

class Shoot(pygame.sprite.Sprite):
    def __init__(self,x,y,dimesions):
        pygame.sprite.Sprite.__init__(self)
        self.anime = []
        for i in range(1,9):
            self.anime.append('images/shoot/bird_explosion_0'+str(i)+'.png')
        self.image = pygame.image.load(self.anime[0])
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x = x + (dimesions[0]/2)
        self.rect.y = y + (dimesions[1]/2)
        self.frame = 0
        self.last_updated = pygame.time.get_ticks()
        self.anim_fps = 60

    def update(self):
        last_updated = pygame.time.get_ticks()
        if last_updated - self.last_updated > self.anim_fps:
            self.last_updated = last_updated
            self.frame += 1
            if self.frame == len(self.anime):
                self.kill()
            else:
                center = self.rect.center
                self.image = pygame.image.load(self.anime[self.frame])
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.rect.x = self.rect.x - 10
        self.rect.y = self.rect.y - 5

cannon = Cannon()
explosion_gp = pygame.sprite.Group()
birds_gp = pygame.sprite.Group()

def gameloop():
    last_pressed = 0  
    cloud_gp = pygame.sprite.Group()
    cannon_gp = pygame.sprite.Group()

    ball_gp = pygame.sprite.Group()

    cannon_gp.add(cannon)

    end = False

    while True:
        clock.tick(60)
        gameDisplay.blit(bg,(0,0))
        timer = random.randint(0, 1250)
        last_updated = pygame.time.get_ticks()

        if timer < 2:
            cloud = Clouds()
            cloud_gp.add(cloud)

        if timer > 3 and timer < 50 and end == False:
            bird = Bird()
            birds_gp.add(bird)

        draw_text('Score: '+str(cannon.score),0,window_height-150,(0,0,0),50)
        draw_text('Bullets left: '+str(cannon.bullets_left),window_width-375,window_height-150,(0,0,0),50)
    #test
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_LEFT:
                    cannon.changed_angle = True
                    cannon.dire = 1
                if event.key==pygame.K_RIGHT:
                    cannon.changed_angle = True
                    cannon.dire = -1
                if event.key==pygame.K_SPACE:
                    space_pressed = pygame.time.get_ticks()

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    if (now-last_pressed)>1000 and cannon.bullets_left > 0:
                        if last_pressed!=0:
                            last_pressed =  now
                            cannon.shoot = True
                            cannon.bullets_left -= 1
                            ball = Ball(cannon.rect.x+(cannon.size[0]/2),cannon.rect.y+(cannon.size[1]/2),cannon.angle)
                            ball.y_power = (now - space_pressed)//70
                            ball_gp.add(ball)
                            pygame.mixer.music.load('Sounds/shoot.mp3')
                            pygame.mixer.music.play()
                            if cannon.bullets_left < 1:
                                end = True
                        else:
                            last_pressed = pygame.time.get_ticks()

        if end == True:
            draw_text('Game over!',(window_width/2)-95,(window_height/2)-95,(0,0,0),50)
            cannon.shoot = False
            for bird in birds_gp:
                bird.kill()
            cannon.kill()

        cloud_gp.update()
        birds_gp.update(ball_gp)
        cannon_gp.update()
        ball_gp.update()
        explosion_gp.update()

        cloud_gp.draw(gameDisplay)
        birds_gp.draw(gameDisplay)
        cannon_gp.draw(gameDisplay)
        ball_gp.draw(gameDisplay)
        explosion_gp.draw(gameDisplay)

        pygame.display.flip()

gameloop()
pygame.quit()
quit()
