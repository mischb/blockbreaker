import pygame as pg, math

class Ball(pg.sprite.Sprite):
  def __init__(self, startPosition):
    super().__init__()
    self.image = pg.transform.scale(pg.image.load('ball.png').convert_alpha(), (20,20))
    alpha = 128
    self.image.fill((255, 255, 255, alpha), None, pg.BLEND_RGBA_MULT)
    self.rect = self.image.get_rect()
    self.rect.x = startPosition[0]
    self.rect.y = startPosition[1]
    self.mask = pg.mask.from_surface(self.image)
    
  def moveBallOnPaddle(self, position):
    self.rect.x = position[0]
    self.rect.y = position[1]
  
  def update(self, vector):
    newpos = self.calcnewpos(self.rect, vector)
    self.rect = newpos

  def calcnewpos(self,rect,vector):
    (angle,z) = vector
    (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
    return rect.move(dx,dy)
