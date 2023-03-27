import pygame

import constants
from constants import images


class Fire:
    def __init__(self, x, y, width, height, gotta_grow_up):
        self.x = x
        self.y = y
        self.frame = 0
        self.image = pygame.image.load(images["fire_0"]).convert_alpha()
        self.width = width
        self.height = height
        self.gotta_grow_up = gotta_grow_up
        self.current_width = width
        self.current_height = height
        self.was_closed = False
        self.is_opened = False

    def display(self, surface):
        div = 5
        if self.was_closed:
            self.current_width = self.width
            self.current_height = self.height
            self.frame = 0
            self.was_closed = False
        self.image = pygame.image.load(images["fire_" + str(self.frame // div)]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.current_width, self.current_height))
        self.image = pygame.transform.rotate(self.image, -90)
        rect = self.image.get_rect(topleft=(self.x, self.y - self.current_width // 2))
        surface.blit(self.image, rect)
        self.frame += 1
        if self.frame == constants.NUMBER_OF_FIRES * div - 1:
            self.frame = 0
            if self.current_width < 85 and self.gotta_grow_up:
                self.current_width += 5
                self.current_height += 10
