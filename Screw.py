import pygame

from constants import images


class Screw:
    def __init__(self, x, y):
        self.image = pygame.image.load(images['screw']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (144 * 800 / 3226 * 0.9, 144 * 800 / 3226 * 0.9))
        self.rect = self.image.get_rect(center=(x, y))
        self.is_spin = False
        self.rotated_image = self.image
        self.new_rect = self.rotated_image.get_rect()
        self.angle = 0

    def display(self, surface):
        if self.is_spin:
            self.angle += 5
        self.rotate_center((self.rect.x, self.rect.y), self.angle)
        surface.blit(self.rotated_image, self.new_rect)
        if self.angle == 360:
            self.angle = 0

    def rotate_center(self, topleft, angle):
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.new_rect = self.rotated_image.get_rect(center=self.image.get_rect(topleft=topleft).center)
