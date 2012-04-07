import pygame
class Sprite:
    def __init__(self, images, fps, loop):
        self.index = 0
        self.timer = 0
        self.images = images
        self.FPS = 1000 / fps
        self.frameCount = len(images)
        self.looping = loop
        self.done = False
        
    def update(self, gameTime):
        if gameTime > self.timer + self.FPS:
            self.timer = gameTime
            self.index += 1
            if self.index + 1 > self.frameCount:
                if self.looping:
                    self.index = 0
                else:
                    self.done = True
                
    def getImage(self):
        if not self.done:
            return self.images[self.index]
        else:
            return pygame.Surface([1,1])
        
        
