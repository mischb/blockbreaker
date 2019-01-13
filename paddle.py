import pygame as pg
class Paddle(pg.sprite.Sprite):
  def __init__(self, color,length, height):
    super().__init__()
    # pg.sprite.Sprite.__init__(self)

    self.image = pg.Surface([length, height])
    self.image.fill(color)
    self.color = color

    pg.draw.line(self.image, self.color, (10, 10), (30, 40))

    self.rect = self.image.get_rect()

  def move_left(self):
    self.rect.x -= 10
  
  def move_right(self):
    self.rect.x += 10