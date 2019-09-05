import pygame
from const import *
import math


class Upgrade_wheel:
    def __init__(self):
        self.pos = ()
        self.rad = 100
        self.base = None
        self.upgrades = [Upgrade_button(), Upgrade_button(), Upgrade_button(), Upgrade_button()]
        self.active = False
        self.color = BLACK
        self.box_selectable = False
        self.button_radius = 60 #  how far the buttons are out from the center
        self.distribution = (2 * math.pi) / len(self.upgrades)

    def switch_active(self, base):
        self.active =not self.active
        if self.active:
            self.base = base
            print(self.base)
            self.pos = self.base.rect.center
            self.place_buttons()

    def process_input(self, events):
        pass

    def update(self):
        pass

    def place_buttons(self):
        for index, button in enumerate(self.upgrades):
            button.pos = (
                int(self.pos[0] + (60 * math.cos(index * self.distribution))),
                int(self.pos[1] + (60 * math.sin(index * self.distribution)))
            )

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, self.pos, self.rad)
            for button in self.upgrades:
                button.draw(screen)



class Upgrade_button:
    def __init__(self):
        self.rad = 20
        self.color = (YELLOW)
        self.pos = ()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
