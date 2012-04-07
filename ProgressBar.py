'''
Created on Nov 6, 2011

@author: Michael
'''
from GameObject import GameObject
import pygame
class ProgressBar(GameObject):
    def __init__(self, x, y, width, height, color):
        self.rect = [x, y, width, height]
        self.percent = 1
        self.max = width
        self.color = color
        
    def update(self, percent):
        self.percent = percent
        self.rect[2] = (self.max * self.percent)
    
    def draw(self, surface):
                
        head = pygame.font.Font(None, 11)         
        text = head.render(str(round(self.percent * 100)) + '%', True, [255,255,255])
        if not self.percent <= 0:
            pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(text, [self.rect[2] + 7, self.rect[1] - 1])
            
        
            
            
        
        

