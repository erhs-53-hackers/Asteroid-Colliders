import pygame
from menu2 import *

WINDOWWIDTH = 700
WINDOWHEIGHT = 600

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sound')


while 1:
	menu = menu2((0, 0, 0), ['start', 'options' 'exit'], 50, 50)
	#for event in pygame.event.get:
	#	if event.type == QUIT:
	#		pygame.quit()
	#		sys.exit()
		
	pygame.display.update()
	


	
