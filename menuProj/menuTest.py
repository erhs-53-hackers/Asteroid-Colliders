import pygame, sys
from Menu import *

def main():
	pygame.init()
	
	screen = pygame.display.set_mode((800, 600))
	
	pygame.display.set_caption("Testing the Menu Class")
	
	menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
                [('Start Game', 1, None)
                #('Controls', 2, None)
                #('Options', 3, None)
                #('Exit', 4, None)])

	#menu.set_center(True, True)
	#menu.set_center(True, True)
	
	#menu.set_alignment('center', 'center')

	#state = 0
	prev_state = 1
	
	while 1:
		if prev_state != state:
			pygame.event.post(pygame.event.Event(EVEN_CHANGE_STATE, key = 0))
			prev_state = state
		
		e = pygame.event.wait()
		
		if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
			if state == 0:
				rect_list, state = menu.update(e, state)
			elif state == 1:
				print('Start Game!')
				state = 0
			elif state == 2:
				print('Controls!')
				state = 0
			elif state == 3:
				print('Options!')
				state = 0
			elif state == 4:
				print('Exit!')
				pygame.quit()
				sys.exit()
				
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit
			
		pygame.display.update(rect_list)
	
__name__ == "__main__"
main()
