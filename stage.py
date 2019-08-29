from const import *
import ai
import levels
import powerbar
import pygame


class Stage():
    def __init__(self):
        # todo make selection tool
        self.ai = ai.Ai(self)
        self.lvl_mngr = levels.Level_mngr(self)
        self.current_level = '1'
        self.bases = self.lvl_mngr.give_lvl(self.current_level)
        self.powerbar = powerbar.Powerbar(100, 100, self.bases)
        self.selected_base = None

        self.clickables = self.bases
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
            if events.mouse.l_clicked:
                for clickable in self.clickables:
                    clickable.process_input(events)

    def update(self):
        print(pygame.mouse.get_pos())
        # code ran if game is not paused. enter all game code in here
        if not self.pause:
            for item in self.drawables:
                item.update()

            self.clickables = self.bases
            self.drawables = [self.powerbar] + self.clickables
            self.ai.update()

    def draw(self, screen):
        screen.fill(NICE_BLUE)
        for drawable in self.drawables:
            drawable.draw(screen)


