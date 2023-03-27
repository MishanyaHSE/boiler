import pygame
import time


from constants import images
from Lever import Lever
from ArrowsController import ArrowsController
from InputBox import InputBox
from ButtonManager import ButtonManager
from TextLabel import TextLabel
from Fire import Fire

BUBBLE_ANIMATION_DURATION = 50



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

        self.off_button_bar_counter = 499

        self.started = False

        # generating bubbles
        startX, startY = self.arrows_controller.pipe_rect.topleft
        endX, endY = self.arrows_controller.pipe_rect.bottomright
        startX += 16
        startY += 30
        endY -= 30
        endX = startX + 11
        self.animCount = BUBBLE_ANIMATION_DURATION
        bubbles = [((x, y), 1) for x in range(startX, endX, 4) for y in range(startY, endY, 7)]
        bubbleSample = bubbles.copy()
        for i in range(1, 5):
            buf = []
            for bubble in bubbleSample:
                point, radius = bubble
                buf.append(((point[0] + i * 46, point[1]), radius))
            bubbles += buf
        self.firstBubbles = bubbles[::2]
        self.secondBubbles = bubbles[1::2]

    def display(self, surface):
        # ALWAYS FIRST
        surface.blit(self.background_img, self.background_rect)
        surface.blit(self.boiler_img, self.boiler_rect)
        #
        if self.button_manager.turn_on.was_pressed and self.check_if_can_start():
            self.started = True
        if self.button_manager.turn_off.was_pressed:
            self.started = False
            self.button_manager.turn_on.was_pressed = False
            for lever in self.levers:
                lever.rotate(lever.x + 1, lever.y + 100)
                self.button_manager.button_bar[self.off_button_bar_counter // 100].to_start_color()
                self.button_manager.button_bar[self.off_button_bar_counter // 100].was_pressed = False
            if self.off_button_bar_counter > 0:
                self.off_button_bar_counter -= 1

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

        if self.button_manager.button_bar[3].was_pressed:
            self.display_bubbles(surface)

        for label in self.labels:
            label.display(surface)

        # LATE ELEMENTS
        for lever in self.levers:
            lever.display(surface)
        if self.big_fire.is_opened and self.small_fire.is_opened:
            self.big_fire.display(surface)
            self.boxes[2].raise_value()
        elif self.boxes[2].is_number() and float(self.boxes[2].text) > 20:
            self.boxes[2].decrease_value()
        if self.small_fire.is_opened:
            self.small_fire.display(surface)
        for label in self.boxes:
            label.display(surface)
        self.button_manager.display(surface)

    def display_bubbles(self, surface):
        self.animCount -= 1
        if not self.animCount:
            self.animCount = BUBBLE_ANIMATION_DURATION
        if self.animCount > BUBBLE_ANIMATION_DURATION / 2:
            for bubble in self.firstBubbles:
                center, radius = bubble
                pygame.draw.circle(surface, (255, 255, 255), center, radius)
        else:
            for bubble in self.secondBubbles:
                center, radius = bubble
                pygame.draw.circle(surface, (255, 255, 255), center, radius)

    def check_if_can_start(self):
        flag = True
        if self.boxes[0].text == '' or not self.boxes[0].text[0].isdigit() or self.boxes[0].text != "0.2":
            flag = False
        if self.boxes[1].text == '' or not self.boxes[1].text[0].isdigit() or self.boxes[1].text != "2":
            flag = False
        return flag
