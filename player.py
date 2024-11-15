import pygame as pg
from body import Body

class Player(Body):
    def __init__(self, x, y, scale, angle, file, speed):
        super().__init__(x, y, scale, angle, file)
        self.speed = speed

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.rect.x += self.speed