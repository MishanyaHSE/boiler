import pygame

from constants import images
from Lever import Lever
from ArrowsController import ArrowsController
from InputBox import InputBox
from ButtonManager import ButtonManager
from TextLabel import TextLabel
from Fire import Fire


class ScreenController:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boiler_img = pygame.image.load(images["boiler"]).convert_alpha()
        self.background_img = pygame.image.load(images["background"]).convert_alpha()
        # move to constants
        self.boiler_img = pygame.transform.scale(self.boiler_img, (width * 0.9, width * 0.9 * 0.6))
        self.background_img = pygame.transform.scale(self.background_img, (width, height))
        self.boiler_rect = self.boiler_img.get_rect(bottomleft=(width * 0.05, height))
        self.background_rect = self.background_img.get_rect(topleft=(0, 0))
        self.levers = []
        lever_1 = Lever(width * 0.215, height * 0.72, width * 0.03125, width * 0.03125 * 0.28)
        lever_2 = Lever(248, 481, 25, 7)
        self.levers.append(lever_1)
        self.levers.append(lever_2)
        self.arrows_controller = ArrowsController()
        self.boxes = []
        self.boxes.append(InputBox(200, 370, 40, 16, "Газ", "м³/час"))
        self.boxes.append(InputBox(150, 230, 40, 16, "Воздух", "м³/час"))
        self.boxes.append(InputBox(724, 240, 40, 16, "Темп. вых.", "°C"))
        self.button_manager = ButtonManager()
        self.labels = [TextLabel(335, 430, "Запальник", 14),
                       TextLabel(390, 433, "ДПЗ", 12),
                       TextLabel(418, 373, "ДПГ", 12)]
        self.big_fire = Fire(346, 392, 20, 40, True)
        self.small_fire = Fire(370, 452, 20, 40, False)

    def display(self, surface):
        # ALWAYS FIRST
        surface.blit(self.background_img, self.background_rect)
        surface.blit(self.boiler_img, self.boiler_rect)

        if self.boxes[2].text != '' and self.boxes[2].text[0].isdigit() and float(self.boxes[2].text) > 39.9:
            surface.blit(self.arrows_controller.pipe_hot_image, self.arrows_controller.pipe_rect)
        else:
            surface.blit(self.arrows_controller.pipe_normal_image, self.arrows_controller.pipe_rect)
        # MID ELEMENTS
        if not self.levers[0].is_opened:
            surface.blit(self.arrows_controller.a_2_w_image, self.arrows_controller.a_2_rect)
            self.big_fire.was_closed = True
            self.big_fire.is_opened = False
        else:
            surface.blit(self.arrows_controller.a_2_y_image, self.arrows_controller.a_2_rect)
            self.big_fire.is_opened = True

        if not self.levers[1].is_opened:
            surface.blit(self.arrows_controller.a_3_w_image, self.arrows_controller.a_3_rect)
            self.small_fire.was_closed = True
            self.small_fire.is_opened = False
        else:
            surface.blit(self.arrows_controller.a_3_y_image, self.arrows_controller.a_3_rect)
            self.small_fire.is_opened = True

        for label in self.labels:
            label.display(surface)

        # LATE ELEMENTS
        for lever in self.levers:
            lever.display(surface)
        for label in self.boxes:
            label.display(surface)
        self.button_manager.display(surface)
        if self.big_fire.is_opened:
            self.big_fire.display(surface)
        if self.small_fire.is_opened:
            self.small_fire.display(surface)
