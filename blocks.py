import pygame as pg


class Block(pg.sprite.Sprite):
    def __init__(self, color, length, height,):
        super().__init__()

        self.image = pg.Surface((length, height))
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
