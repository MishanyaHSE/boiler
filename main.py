import pygame as pg

import constants
from ScreenController import ScreenController


WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.update()
screen_control = ScreenController(WIDTH, HEIGHT)
pg.display.set_caption('')
icon = pg.image.load(constants.images["fire_0"]).convert_alpha()
pg.display.set_icon(icon)
clock = pg.time.Clock()

# image to rotate DElETE THIS ON ARRIVAL
sm_image = pg.image.load(constants.images["fire_0"]).convert_alpha()

running = True
doMove = False
white = False
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
        if screen_control.started:
            for lever in screen_control.levers:
                lever.handle_event(i)
            for button in screen_control.button_manager.button_bar:
                button.handle_event(i)
        else:
            screen_control.button_manager.turn_on.handle_event(i)
            for label in screen_control.boxes:
                label.handle_event(i)
    screen_control.display(screen)
    clock.tick(60)
    pg.display.update()
