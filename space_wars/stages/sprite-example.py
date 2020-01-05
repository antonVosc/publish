import pygame

width = 800
hight = 600
FPS = 60
black = (0,0,0)
green = (0,255,0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,hight))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario.png").convert()
        #self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,hight/2)
    def left(self):
        self.rect.x -=5
    def right(self):
        self.rect.x +=5


run = True
all_sprites = pygame.sprite.Group()
igrok = Player()
ed = Player()
all_sprites.add(igrok)
all_sprites.add(ed)
ed.rect.x = 200
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                igrok.left()
                ed.right()
            if event.key==pygame.K_RIGHT:
                igrok.right()
                ed.left()

    all_sprites.update()
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
quit()
