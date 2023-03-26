import pygame

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('green')
COLOR_TEXT = pygame.Color('green')
BACK_COLOR = pygame.Color('beige')
HOVER_COLOR = pygame.Color('moccasin')


class InputBox:
    def __init__(self, x, y, w, h, name, quantity, text='0.00'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.f1 = pygame.font.SysFont('Arial', 12)
        self.txt_surface = self.f1.render(text, True, COLOR_TEXT)
        self.active = False
        self.name = name
        self.name_surface = self.f1.render(name, True, 'black')
        self.name_rect = self.name_surface.get_rect()
        self.quantity_surface = self.f1.render(quantity, True, 'black')
        self.first_touch = True
        self.back_color = BACK_COLOR

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.first_touch:
                    self.first_touch = False
                    self.text = ''
                    self.txt_surface = self.f1.render(self.text, True, COLOR_TEXT)
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.back_color = HOVER_COLOR
            else:
                self.back_color = BACK_COLOR
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif (event.unicode.isdigit() or event.unicode == ".") and len(self.text) < 5:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.f1.render(self.text, True, COLOR_TEXT)

    def display(self, surface):
        pygame.draw.rect(surface, 'grey', (self.rect.x + 2, self.rect.y + 2, self.rect.width, self.rect.height))
        pygame.draw.rect(surface, self.back_color, self.rect)
        surface.blit(self.name_surface, (self.rect.x + self.rect.width // 2 - self.name_rect.width // 2,
                                        self.rect.y - 15))
        surface.blit(self.quantity_surface, (self.rect.x + self.rect.width + 5, self.rect.y + 3))
        surface.blit(self.txt_surface, (self.rect.x + self.rect.width // 2 - self.txt_surface.get_rect().width // 2,
                                       self.rect.y + self.rect.height // 2 - self.txt_surface.get_rect().height // 2))
        pygame.draw.rect(surface, self.color, self.rect, 1)
