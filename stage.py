from const import *
import ai
import levels
import powerbar
import pygame
import selection_box
import upgrade_wheel


class Stage():
    def __init__(self):
        self.ai = ai.Ai(self)
        self.current_level = 'test'
        self.bases = levels.create_lvl(self, self.current_level)

        self.powerbar = powerbar.Powerbar(100, 100, self.bases)
        self.upgrade_wheel = upgrade_wheel.Upgrade_wheel()

        self.selected_base = None

        self.selection_box = selection_box.Selection_box()
        self.clickables = self.bases + [self.upgrade_wheel, self.selection_box]
        self.selection_box.load_selectables(self.clickables)

        self.drawables = [self.powerbar] + self.clickables
        self.pause = False



    def select_building(self, base):
        if self.selected_base:
            self.selected_base.transfer_creatures(base)
            self.selected_base.set_selected()
            self.selected_base = None
        else:
            base.set_selected()
            self.selected_base = base

    def process_input(self, events):
        # detects if game is paused
        if events.keyboard.key_down(pygame.K_SPACE):
            self.pause =not self.pause

        # code ran if game is not paused. enter all keys in here
        if not self.pause:
            for clickable in self.clickables:
                clickable.process_input(events)

    def update(self):


        # code ran if game is not paused. enter all game code in here
        if not self.pause:
            self.ai.update()
            self.clickables = self.bases + [self.upgrade_wheel, self.selection_box]
            # todo: refactor code so that drawables doesn't have to be declared twice
            self.drawables = [self.powerbar] + self.clickables


            for item in self.drawables:
                item.update()

    def draw(self, screen):
        # print(pygame.mouse.get_pos())
        screen.fill(NICE_BLUE)
        for drawable in self.drawables:
            drawable.draw(screen)


