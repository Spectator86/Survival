from settings import *
import pygame as pg
from player import Player

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Survival Game")

clock = pg.time.Clock()

player = Player(WIDTH//2, HEIGHT//2, 100, 0, "images/hero.png", 10)

while True:
    sc.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    player.draw(sc)
    player.control()

    clock.tick(FPS)
    pg.display.update()