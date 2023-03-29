import pygame


class TextLabel:
    def __init__(self, x, y, text, text_size):
        self.x = x
        self.y = y
        self.f1 = pygame.font.Font(None, text_size)
        self.txt_surface = self.f1.render(text, True, 'black')

    def display(self, surface):
        surface.blit(self.txt_surface, (self.x, self.y))
