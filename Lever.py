import math
import pygame

from constants import images


class Lever:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(images["lever"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rotated_image = self.image
        self.last_angle = 0
        self.circle_image = pygame.image.load(images["circle"]).convert_alpha()
        self.circle_image = pygame.transform.scale(self.circle_image, (self.width*2, self.width*2 + self.width*0.2))
        self.base_image = pygame.image.load(images["base"]).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (self.height * 1.5, self.width * 3))
        self.opening_percent = 0
        # грузим картинку
        self.rect = self.image.get_rect(
            topleft=(self.x, self.y)  # расположение картинки относительно левой верхней точки с указанием координат
        )
        self.is_opened = False
        self.is_movable = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            rect = self.rect
            if rect.collidepoint(pos):
                self.is_movable = True
        if event.type == pygame.MOUSEBUTTONUP and self.is_movable:
            self.is_movable = False
        if event.type == pygame.MOUSEMOTION and self.is_movable:
            pos = pygame.mouse.get_pos()
            self.rotate(pos[0], pos[1])

    def display(self, surface):
        self.rect = self.rotated_image.get_rect(
            topleft=(self.x, self.y)
        )
        circle_rect = self.circle_image.get_rect(
            center=(self.x + self.width / 4, self.y)
        )
        base_rect = self.base_image.get_rect(
            center=circle_rect.center
        )
        surface.blit(self.base_image, base_rect)
        surface.blit(self.rotated_image, self.rect)
        surface.blit(self.circle_image, circle_rect)

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def find_angle(self, x, y):
        x_0 = self.x
        y_0 = self.y
        if x - x_0 != 0:
            angle = math.atan((y - y_0) / (x - x_0))
            angle = math.degrees(angle)
        else:
            return self.last_angle
        self.last_angle = 90 - angle
        return 90 - angle

    def update_percent(self, angle):
        self.opening_percent = angle / 90 * 100
        if self.opening_percent < 4:
            self.opening_percent = 0
        if self.opening_percent > 99:
            self.opening_percent = 100
        if self.opening_percent != 0:
            self.is_opened = True
        else:
            self.is_opened = False

    def rotate(self, x, y):
        angle = self.find_angle(x, y)
        if 0 <= angle <= 90:
            self.rotated_image = pygame.transform.rotate(self.image, angle)
            self.update_percent(angle)
        #     хз надо ли
        # elif 0 < angle <= 4:
        #     self.rotated_image = self.image
        # elif 88 <= angle <= 90:
        #     self.rotated_image = pygame.transform.rotate(self.image, 90)

