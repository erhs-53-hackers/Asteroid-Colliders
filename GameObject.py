'''
Created on Nov 1, 2011

@author: Michael
'''
from Sprite import Sprite
from pygame import Rect
import pygame


class GameObject:
    def __init__(self, x, y, width, height, images, fps, looping):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = Sprite(images, fps, looping)        
        
    def update(self, gameTime):
        self.sprite.update(gameTime)
        
    def draw(self, surface):
        surface.blit(self.getImage(), self.getRect())        
        
    def getRect(self):
        return Rect(self.x, self.y, self.width, self.height)
    
    def getImage(self):
        return self.sprite.getImage()
    
    def setSprite(self, sprite):
        self.sprite = sprite
    
    def getHitMask(self):        
        return pygame.surfarray.array_alpha(self.sprite.getImage())
