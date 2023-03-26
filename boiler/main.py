import pygame as pg

from constants import images
from Lever import Lever
from ScreenController import ScreenController

WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.update()
scrn_cntrl = ScreenController(WIDTH, HEIGHT)

running = True
doMove = False
white = False
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
        if i.type == pg.MOUSEBUTTONDOWN:
            pos = i.pos
            print(pos)
        for lever in scrn_cntrl.levers:
            lever.handle_event(i)
        for label in scrn_cntrl.boxes:
            label.handle_event(i)
        for button in scrn_cntrl.button_manager.button_bar:
            button.handle_event(i)
    scrn_cntrl.display(screen)
    pg.display.update()
