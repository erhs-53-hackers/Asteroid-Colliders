'''
Created on Oct 23, 2011

@author: Michael
'''

from GameObject import GameObject
import pygame
from Shield import Shield
from Sprite import Sprite

class Player(GameObject):
    
    def __init__(self, x, y, width, height, fps):
        images = []
        images.append(pygame.image.load('res/image/player.png'))
        images.append(pygame.image.load('res/image/player2.png'))
        super().__init__(x, y, width, height, images, fps, True)
        self.lives = 3   
        self.isShield = False 
        self.shield = Shield(0, 0, 70, 70, 1)
        self.timer = 0
        self.shieldExpended = False
        
        images2 = []
        images2.append(pygame.image.load('res/image/exp1.png'))
        images2.append(pygame.image.load('res/image/exp2.png'))
        images2.append(pygame.image.load('res/image/exp3.png'))
        images2.append(pygame.image.load('res/image/exp4.png'))
        images2.append(pygame.image.load('res/image/exp5.png'))
        images2.append(pygame.image.load('res/image/exp6.png'))
        images2.append(pygame.image.load('res/image/exp7.png'))
        images2.append(pygame.image.load('res/image/exp8.png'))
        images2.append(pygame.image.load('res/image/exp9.png'))
        images2.append(pygame.image.load('res/image/exp10.png'))
        images2.append(pygame.image.load('res/image/exp11.png'))
        images2.append(pygame.image.load('res/image/exp12.png'))
        images2.append(pygame.image.load('res/image/exp13.png'))
        images2.append(pygame.image.load('res/image/exp14.png'))
        images2.append(pygame.image.load('res/image/exp15.png'))
        images2.append(pygame.image.load('res/image/exp16.png'))
        images2.append(pygame.image.load('res/image/exp17.png'))
        
        self.explosion = Sprite(images2, 15, False)
    
    def update(self, gameTime):       
        super().update(gameTime)
        self.shield.x = self.x - 3
        self.shield.y = self.y - 3
        if self.isShield:
            self.timer += 1
            if self.timer > self.shield.timeLimit:
                self.isShield = False
                self.shieldExpended = True                
                
    def draw(self, surface):
        super().draw(surface)
        if self.isShield:
            surface.blit(self.shield.getImage(), self.shield.getRect())
            
    def explode(self):
        self.setSprite(self.explosion)
        
   
         
        
        
                 
        
