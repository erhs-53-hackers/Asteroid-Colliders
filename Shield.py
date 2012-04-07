'''
Created on Nov 5, 2011

@author: Michael
'''
from GameObject import GameObject
import pygame
class Shield(GameObject):    
    def __init__(self, x, y, width, height, fps):
        images = []
        images.append(pygame.image.load('res/image/shield.png'))
        super().__init__(x, y, width, height, images, fps, True)
        self.timeLimit = 260
        