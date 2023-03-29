import pygame

START_COLOR = pygame.Color('grey')
CORRECT_COLOR = pygame.Color('green')
WRONG_COLOR = pygame.Color('red')


class Button:
    def __init__(self, x, y, width, height, text, name, text_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.name = name
        self.f1 = pygame.font.SysFont('Arial', text_size)
        self.txt_surface = self.f1.render(text, True, 'black')
        self.name_surface = self.f1.render(name, True, 'black')
        self.color = START_COLOR
        self.previous_clicked = False
        self.was_pressed = False
        self.is_on = False
        self.is_off = False
        self.add_frame = False
        self.frame_color = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_on or self.is_off:
                if self.rect.collidepoint(event.pos):
                    self.was_pressed = True
            else:
                if self.rect.collidepoint(event.pos):
                    if self.previous_clicked:
                        self.color = CORRECT_COLOR
                        self.was_pressed = True
                    else:
                        self.color = WRONG_COLOR

    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.name_surface, (self.rect.x + self.rect.width // 2 - self.name_surface.get_rect().width // 2,
                                         self.rect.y + self.rect.height // 2 - self.name_surface.get_rect().height // 2))
        surface.blit(self.txt_surface, (self.rect.x + self.rect.width + 5, self.rect.y))
        if self.add_frame:
            pygame.draw.rect(surface, self.frame_color, self.rect, 2)

    def to_start_color(self):
        self.color = START_COLOR
