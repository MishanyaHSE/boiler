import pygame as pg

from Lever import Lever
import constants

WHITE = (255, 255, 255)
BLUE = (0, 0, 225)

pg.init()
sc = pg.display.set_mode((800, 600))
sc.fill(WHITE)
pg.display.update()
lever = Lever(100, 100, 35, 5)
levers = [lever]

running = True
doMove = False
while running:
    sc.fill(WHITE)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
        if i.type == pg.MOUSEBUTTONDOWN:
            for lev in levers:
                pos = pg.mouse.get_pos()
                rect = lev.rect
                if rect.collidepoint(pos):
                    doMove = True
                    cur_lever = lev
        if i.type == pg.MOUSEBUTTONUP and doMove:
            doMove = False
        if i.type == pg.MOUSEMOTION and doMove:
            pos = pg.mouse.get_pos()
            cur_lever.rotate(pos[0], pos[1])
    lever.display(sc)
    pg.display.update()
