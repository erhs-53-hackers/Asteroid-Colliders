'''
Created on Nov 4, 2011

@author: Michael
'''
def collideRect(rect1, rect2):
        if rect1.colliderect(rect2):
            return True
        else:
            return False
def collide(sp1,sp2):
    """
    Internal method used for pixel perfect collision detection.
    """
    rect1 = sp1.getRect()  
    rect2 = sp2.getRect()
    
    if collideRect(rect1, rect2):
        
                                   
        rect  = rect1.clip(rect2)
                    
        hm1 = sp1.getHitMask()
        hm2 = sp2.getHitMask()
            
        x1 = rect.x-rect1.x
        y1 = rect.y-rect1.y
        x2 = rect.x-rect2.x
        y2 = rect.y-rect2.y
        for r in range(0,rect.height):
            for c in range(0,rect.width):
                if hm1[c+x1][r+y1] & hm2[c+x2][r+y2]:
                    return True        

    return False
