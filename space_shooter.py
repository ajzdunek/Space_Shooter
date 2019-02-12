import pygame
import sys
import random


pygame.init()

pygame.font.init() #our font


w_width = 800 # Set window width
w_height = 600 # Set window height


black = (0, 0, 0) #background
white = (255, 255, 255)
gray = (105, 105, 105)
orange = (255, 127, 80) #lasers

all_sprites = pygame.sprite.Group() # Create a sprite group
asteroids = pygame.sprite.Group()
lasers = pygame.sprite.Group()


class SpaceShip(pygame.sprite.Sprite):


    '''Load spaceship image'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('SpaceShipSmall.png').convert()

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
        self.rect.x += self.speed_x

        '''Prevents ship from going off screen
        and quiting the game'''
        if self.rect.right > w_width: #right side of the screen
            self.rect.right = w_width

        if self.rect.left < 0: #eft side of the screen
            self.rect.left = 0


    def fire_laser(self):
        laser = Lasers(self.rect.x + 35, self.rect.y) # create a laser object at the ships location.
        all_sprites.add(laser) # add to all_sprites group
        lasers.add(laser) # add to laser sprites group


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



class Lasers(pygame.sprite.Sprite):

    '''Shooting the enemy asteroids'''

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 15))
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x
        self.speed_y = -20 #negative because lasers need to fire upwards


    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0: # will make it so if laser goes off screen it will be deleted.
            self.kill()



'''Creating the gameplay loop'''
''' THIS IS THE CORE OF OUR FUNCTIONALITY'''

def gameplay():

    spaceshipwidth = 75

    '''Set the game display 
    width and height'''
    gameDisplay = pygame.display.set_mode((w_width, w_height))

    '''Set the title
     of the game'''
    pygame.display.set_caption('Space Wars')

    clock = pygame.time.Clock()

    '''font and font set for score'''
    sfont = pygame.font.SysFont('Arial', 20)
    score = 0

    '''creating the player object'''
    player = SpaceShip()
    all_sprites.add(player)


    ''' make asteroids/sprites'''

    for i in range(15):
        a = Asteroids()
        all_sprites.add(a)
        asteroids.add(a)


    '''Finishing up and staring the game'''
    exitGame = False

    while exitGame == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.fire_laser()


            print(event) #monitor events in the console
        all_sprites.update()


        collide = pygame.sprite.spritecollide(player, asteroids, False)


        destroy_asteroid = pygame.sprite.groupcollide(asteroids, lasers, True, True )


        for col in range(len(destroy_asteroid)): #regenerates more asteroids
            score += 1
            a2 = Asteroids()
            all_sprites.add(a2)
            asteroids.add(a2)


        if len(collide) > 0: # Checking if list has any values and exiting game if true.
            exitGame = True


        gameDisplay.fill(black)
        all_sprites.draw(gameDisplay)
        player_score = sfont.render('Score: ' + str(score), False, (0, 255, 127)) #render the score with text color, False is for alias.
        gameDisplay.blit(player_score, (1, 20)) #blit the score onto the screen upper right hand corner
        pygame.display.flip()

        clock.tick(60) #frames per second


gameplay()
pygame.quit()
sys.exit()