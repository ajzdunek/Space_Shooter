import pygame
import sys
import random


pygame.init()


w_width = 800 # Set window width
w_height = 600 # Set window height


black = (0, 0, 0) #background
white = (255, 255, 255)
gray = (105, 105, 105)
orange = (255, 127, 80) #lasers

all_sprites = pygame.sprite.Group() # Create a sprite group
asteroids = pygame.sprite.Group()


class SpaceShip(pygame.sprite.Sprite):


    '''Load spaceship image'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('SpaceShipSmall.png').covert()

        '''making our asteroids and its behavior'''

        self.rect = self.image.get_rect()
        self.rect.x = w_width * 0.25
        self.rect.y = w_height * 0.9
        self.speed_x = 0

        '''Controlling our game'''
    def update(self):
        self.speed_x = 0
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_LEFT]:
            self.speed_x = -10
        if keypress[pygame.K_RIGHT]:
            self.speed_x = 10
        self.rect.x = self.speed_x

        '''Prevents ship from going off screen
        and quiting the game'''
        if self.rect.right > w_width: #right side of the screen
            self.rect.right = w_width

        if self.rect.left < 0: #left side of the screen
            self.rect.left = 0


class Asteroids(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        r = random.randint(20, 60)
        self.image = pygame.Surface((r, r))
        self.image.fill(gray)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, w_width)
        self.rect.y = -600
        self.speed_y = random.randrange(5, 8)


    def update(self):

        '''update the position of the asteroid
        based on the random speed'''

        self.rect.y += self.speed_y
        if self.rect.y > w_height:
            self.rect.x = random.randrange(0, w_width)
            self.rect.y = -600
            self.speed_y = random.randrange(5, 8)



'''Creating the gameplay loop'''

def gameplay():

    spaceshipwidth = 75

    '''Set the game display 
    width and height'''
    gameDisplay = pygame.display.set_mode((w_width, w_height))

    '''Set the title
     of the game'''
    pygame.display.set_caption('Space Wars')

    clock = pygame.time.Clock()

    '''font set for score'''
    sfont = pygame.font.SysFont('Arial', 20)

    '''creating the player object'''
    player = SpaceShip()
    all_sprites.add(player)


    ''' make asteroids/sprites'''

    for i in range(15):
        a = Asteroids()
        all_sprites.add(a)
        asteroids.add(a)



    exitGame = False

    while exitGame == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True

        print(event) #monitor the console

        clock.tick(60) #frames per second


gameplay()
pygame.quit()
sys.exit()
