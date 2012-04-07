'''
Created on 2011.11.3
@author: Nick Yaculak 
(c) Yaculak and Stevens, inc
nyaculak@gmail.com
'''

from Sprite import *
from GameObject import *
import pygame


class Laser(GameObject):
    def __init__(self, speed, x, y, width, height, fps):
        laserImage = []
        laserImage.append(pygame.image.load('res/image/laser.png'))
        super().__init__(x, y, width, height, laserImage, fps, True)
        self.speed = speed  
        
    def update(self, gameTime):
        super().update(gameTime)
        self.y -= self.speed

