



import pygame, sys

class menu2:
	state = 0


	def __init__(self, screenCol, opt, x, y):
		self.screenCol = screenCol
		self.opt = opt
		self.x = x
		self.y = y
		
	def menu2(self):
		i = 0
		while 1:
			pygame.screen.fill(self.screenCol)
			for j in range(0, len(self.opt)):
				if j == i:
					screen.blit(font2.render(self.opt[j], True, (0, 255, 255)), (self.x, self.y))
				else: 
					screen.blit(font2.render(self.opt[j], True (255, 255, 255)), (self.x, self.y))
				self.y += 100
			for e in pygame.event.get:
				if e.type == QUIT:
					exit()
				elif e. type == KEYDOWN:
					if e.type == K_UP:
						i -= 1
						if i > 3: i = 0
					elif e.key == K_DOWN:
						i += 1
						if i > 3:
							i = 0
					# elif e.key == K_RETURN:
						# if i == 0:
							# return state = 1
						# for i in range(0, 1000):
							# return i + 1
			pygame.display.update()
					