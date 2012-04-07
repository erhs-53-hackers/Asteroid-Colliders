'''
Created on Oct 29, 2011

@author: Michael

'''

from GameObject import GameObject
import pygame
class Asteroid(GameObject):
    
        
    def __init__(self, speed, x, y, width, height, fps):
        asteroidImage = []
        asteroidImage.append(pygame.image.load('res/image/ast6.png'))
        asteroidImage.append(pygame.image.load('res/image/ast5.png'))
        asteroidImage.append(pygame.image.load('res/image/ast4.png'))
        asteroidImage.append(pygame.image.load('res/image/ast3.png'))
        asteroidImage.append(pygame.image.load('res/image/ast2.png'))
        asteroidImage.append(pygame.image.load('res/image/ast1.png'))
        
        super().__init__(x, y, width, height, asteroidImage, fps, True)
        self.speed = speed 
    
    
    def update(self, gameTime):
        super().update(gameTime)
        self.y += self.speed
        
            
        
   
    
        
        

    
    
    
