''' Asteroid Colliders
 - @ authors Nick Yaculak & Michael Stevens
 - Released under the GNU General Public License 3
 '''
 
import pygame, sys, time, random
from pygame.locals import *
from Player import *
from Asteroid import *
from Laser import *
import random
from CollisionDetection import collide
import dumbmenu as dm
from ProgressBar import ProgressBar

# set up pygame, window, and colors
pygame.init()
mainClock = pygame.time.Clock()
WINDOWWIDTH = 700
WINDOWHEIGHT = 600
size = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(size)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Asteroid Colliders')
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set up the block data structure
livesImage = pygame.transform.smoothscale(pygame.image.load('res/image/player.png'), [45,45])

MOVESPEED = 10
 
player = Player(MOVESPEED, size, 64, 64, 8)

asteroids = []
asteroidCounter = 0
NEWASTEROID = 40

lasers = []
laserCounter = 0
laserTimer = 0

ScoreTimer = 0
Score = 0
Timer = 0
CYCLECOUNTER = 0

# set up keyboard variables
isMoveLeft = False
isMoveRight = False
isMoveUp = False
isMoveDown = False

oneThird = 1/3

# set up music
kaboomSound = pygame.mixer.Sound('res/sound/kaboom.wav')
laserSound = pygame.mixer.Sound('res/sound/laser_blast.wav')
pygame.mixer.music.load('res/sound/background.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

laserBar = ProgressBar(5, 5, 200, 5, [255,0,0])
shieldBar = ProgressBar(5, 15, 200, 5, [0,0,255])
healthBar = ProgressBar(5, 25, 200, 5, [0, 255, 0])
        
def checkQuit(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
def quit():
    pygame.quit()
    sys.exit()
        
def addAsteroid():
    global asteroidCounter
    global WINDOWWIDTH
    asteroidCounter += 1
    if asteroidCounter >= NEWASTEROID:
        # add new asteroid
        asteroidCounter = 0
        foo = Asteroid(random.randrange(10, 17), random.randrange(0, WINDOWWIDTH - 64), -64, 64, 64, 5)
        asteroids.append(foo)
def addLaser():
    global laserCounter
    global player
    laser = Laser(20, player.x, player.y, 15, 82, 10)
    
    if laserCounter < 30:
        laserCounter += 1
        laser.x = player.x + (player.width / 2) - (laser.width / 2)
        laser.y = player.y - laser.height
        lasers.append(laser)
        laserSound.play()
                
playGame = 0

def showControls():
    while 1:
        pygame.display.update()
        pygame.display.set_caption('Controls')
        pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        screen.fill(BLACK)
        
        # Create a font
        head = pygame.font.Font(None, 50)
        
        # Render the text
        text = head.render('Powered by Python and PyGame', True,
        GREEN, BLACK)
        text2 = head.render('These are the game controls', True, GREEN,
        BLACK)
        
        # Create a rectangle
        textRect = text.get_rect()
        text2Rect = text2.get_rect()
        
        # Center the rectangle
        textRect.centerx = screen.get_rect().centerx
        textRect.y = screen.get_rect().y
        
        x = 100
        y = 100
        
        text2Rect.x = screen.get_rect().x
        text2Rect.y = screen.get_rect().y
        
        # Blit the text
        screen.blit(text, textRect)
        #screen.blit(text2, text2Rect)
        
        pygame.display.quit
        
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mainMenu()
                 
def pauseMenu():
    global musicPlaying
    while 1:
        #558, 90
        # title = pygame.image.load('res/image/title.png')
        # titlerect = title.get_rect(center=(350, 300))
        # screen.blit(title, titlerect)
        # pygame.display.flip()
        choose = dm.dumbmenu(screen, [
                            'Resume Game',
                            'Quit Game'], 64, 64, None, 32, 1.4, GREEN, GREEN)
        if choose == 0:
            print('Resuming Game!')
            global playGame
            playGame = 1
            break
        if choose == 1:
            print('Exiting Game!')
            quit()
                 
def mainMenu():
    global musicPlaying
    while 1:
        screen.fill(BLACK)
    #558, 90
        title = pygame.image.load('res/image/title.png')
        titlerect = title.get_rect(center=(350, 300))
        screen.blit(title, titlerect)
        pygame.display.flip()
        choose = dm.dumbmenu(screen, [
                            'Start Game',
                            'Options',
                            'Controls',
                            'Highscores',
                            'Quit Game',
                            'Toggle Music'], 375, 400, None, 32, 1.4, GREEN, GREEN, True)
        if choose == 0:
            print('Starting Game!')
            global playGame
            playGame = 1
            break
        if choose == 1:
            print('Showing options!')
            #showOptions()
        if choose == 2:
            print('Showing controls!')
            showControls()
        if choose == 3:
            print('Showing highscores!')
            #showHighscores()
        if choose == 4:
            print('Exiting Game')
            quit()
        if choose == 5:
            if musicPlaying:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1, 0.0)
            musicPlaying = not musicPlaying

mainMenu()

# run the game loop
while playGame == 1:
    for event in pygame.event.get():
        checkQuit(event)
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                player.moveLeft(True)
            if event.key == K_RIGHT or event.key == ord('d'):
                player.moveRight(True)
            if event.key == K_UP or event.key == ord('w'):
                player.moveUp(True)
            if event.key == K_DOWN or event.key == ord('s'):
                player.moveDown(True)
            if event.key == ord('f'):
                addLaser()
            if event.key == ord('p'):
                pauseMenu()           
            if event.key == K_SPACE:
                if player.isShield:
                    player.isShield = False
                else:
                    player.isShield = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                player.moveLeft(False)                
            if event.key == K_RIGHT or event.key == ord('d'):
                player.moveRight(False)
            if event.key == K_UP or event.key == ord('w'):
                player.moveUp(False)
            if event.key == K_DOWN or event.key == ord('s'):
                player.moveDown(False)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
    
    windowSurface.fill(BLACK)    

    # if player has lives remaining, draw player
	# else, make him explode upon impact
    if player.lives > 0:
        player.update(pygame.time.get_ticks())
        player.draw(windowSurface)
    else:
        player.explode()
        if player.sprite.done:
            quit()

    # draw the asteroids
    addAsteroid()   
    for asteroid in asteroids:
        asteroid.update(pygame.time.get_ticks())
        asteroid.draw(windowSurface)

    # draw the lasers
    for laser in lasers:
        laser.draw(windowSurface)
        laser.update(pygame.time.get_ticks())

    # check if a laser collides with an asteroid
    for laser in lasers:
        for asteroid in asteroids:
            if(collide(laser, asteroid)):
                #lasers.remove(laser)
                asteroids.remove(asteroid)
                kaboomSound.play()
        if laser.y < 0 - laser.height:
            lasers.remove(laser)

	# check if the player has collided with an asteroid
    for asteroid in asteroids:
        c = False
        if player.isShield:
            c = collide(player.shield, asteroid)
        else:
            c = collide(player, asteroid)
        if c:
            asteroids.remove(asteroid)
            if not player.isShield:
                player.lives -= 1;
            if musicPlaying:
                kaboomSound.play()

    Timer += 1
    if Timer > 500:
        NEWASTEROID /= 1.2
        CYCLECOUNTER += 1
        Timer = 0
    
    laserTimer += 1
    if laserTimer > 500 and laserCounter != 0:
        laserCounter -= 1
        laserTimer = 0

    ScoreTimer += 1
    if ScoreTimer > 50:
        Score += 1
        ScoreTimer = 0

    #draw lives and other player information bars
    for life in range(0, player.lives):
        windowSurface.blit(livesImage, [livesImage.get_height()*life, WINDOWHEIGHT - livesImage.get_height()])
        
    laserBar.update((30 - laserCounter)/30)
    laserBar.draw(windowSurface)
    
    shieldBar.update((player.shield.timeLimit - player.timer)/player.shield.timeLimit)
    shieldBar.draw(windowSurface)
        
    healthBar.update(player.lives / 3)
    healthBar.draw(windowSurface)

    head = pygame.font.Font(None, 20)
    text = head.render("Score: " + str(Score), True, [255,255,255])
    windowSurface.blit(text, [30, 50])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
