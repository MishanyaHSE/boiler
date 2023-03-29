import pygame

from constants import images

WIDTH_SCALE = 800 / 3226 * 0.9
HEIGHT_SCALE = 800 / 1718 * 0.54


class ArrowsController:
    def __init__(self):
        self.a_1_w_image = pygame.image.load(images["a_1_w"]).convert_alpha()
        self.a_1_w_image = pygame.transform.scale(self.a_1_w_image, (171 * WIDTH_SCALE, 301 * HEIGHT_SCALE))
        self.a_1_rect = self.a_1_w_image.get_rect(bottomright=(78, 444))
        self.a_1_y_image = pygame.image.load(images["a_1_y"]).convert_alpha()
        self.a_1_y_image = pygame.transform.scale(self.a_1_y_image, (171 * WIDTH_SCALE, 301 * HEIGHT_SCALE))

        self.a_2_w_image = pygame.image.load(images["a_2_w"]).convert_alpha()
        self.a_2_w_image = pygame.transform.scale(self.a_2_w_image, (595 * WIDTH_SCALE, 159 * HEIGHT_SCALE))
        self.a_2_rect = self.a_2_w_image.get_rect(topright=(306, 400))
        self.a_2_y_image = pygame.image.load(images["a_2_y"]).convert_alpha()
        self.a_2_y_image = pygame.transform.scale(self.a_2_y_image, (595 * WIDTH_SCALE, 159 * HEIGHT_SCALE))

        self.a_3_w_image = pygame.image.load(images["a_3_w"]).convert_alpha()
        self.a_3_w_image = pygame.transform.scale(self.a_3_w_image, (493 * WIDTH_SCALE, 113 * HEIGHT_SCALE))
        self.a_3_rect = self.a_3_w_image.get_rect(bottomright=(361, 486))
        self.a_3_y_image = pygame.image.load(images["a_3_y"]).convert_alpha()
        self.a_3_y_image = pygame.transform.scale(self.a_3_y_image, (493 * WIDTH_SCALE, 113 * HEIGHT_SCALE))

        self.pipe_normal_image = pygame.image.load(images["pipe_normal"]).convert_alpha()
        self.pipe_normal_image = pygame.transform.scale(self.pipe_normal_image, (1434 * WIDTH_SCALE, 1651 * HEIGHT_SCALE))
        self.pipe_rect = self.pipe_normal_image.get_rect(bottomleft=(440, 600))
        self.pipe_hot_image = pygame.image.load(images["pipe_hot"]).convert_alpha()
        self.pipe_hot_image = pygame.transform.scale(self.pipe_hot_image, (1434 * WIDTH_SCALE, 1651 * HEIGHT_SCALE))
