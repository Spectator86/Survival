import pygame as pg

class Body:
    def __init__(self, x, y, scale, angle, file):
        self.image = pg.image.load(file).convert_alpha()
        self.image = pg.transform.scale(self.image, (scale, scale))
        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, sc):
        sc.blit(self.image, (self.rect.x, self.rect.y))

    def resize(self, scalex, scaley):
        self.image = pg.transform.scale(self.image, (scalex, scaley))
        self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))