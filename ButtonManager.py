import pygame
from Button import Button


class ButtonManager:
    def __init__(self):
        self.button_bar = []
        self.button_bar.append(Button(493, 21, 15, 15, "Давление топлива", '', 14))
        self.button_bar.append(Button(493, 46, 15, 15, "Напор воздуха", '', 14))
        self.button_bar.append(Button(493, 71, 15, 15, "Разрежение в топке", '', 14))
        self.button_bar.append(Button(493, 96, 15, 15, "Циркуляция котла", '', 14))
        self.button_bar.append(Button(493, 121, 15, 15, "Пламя горелки", '', 14))
        self.button_bar[0].previous_clicked = True
        self.turn_on = Button(48, 38, 70, 25, '', "Пуск", 20)
        self.turn_on.is_on = True
        self.turn_off = Button(132, 38, 70, 25, '', "Стоп", 20)
        self.turn_off.is_off = True
        self.button_bar.append(self.turn_on)
        self.button_bar.append(self.turn_off)

    def add_button(self, button):
        self.button_bar.append(button)

    def display(self, surface):
        for i in range(5):
            can_be_pressed = True
            for j in range(i):
                if not self.button_bar[j].was_pressed:
                    can_be_pressed = False
            self.button_bar[i].previous_clicked = can_be_pressed
        for button in self.button_bar:
            button.display(surface)
        self.turn_on.display(surface)
        self.turn_off.display(surface)
