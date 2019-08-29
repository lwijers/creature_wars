from const import *
import base
import ai
import random
import levels


class Stage():
    def __init__(self):
        # todo make selection tool
        self.ai = ai.Ai(self)
        self.lvl_mngr = levels.Level_mngr(self)
        self.current_level = '1'
        self.bases = self.lvl_mngr.give_lvl(self.current_level)

        self.selected_base = None

        self.clickables = self.bases
        self.drawables = self.clickables

    def select_building(self, base):
        if self.selected_base:
            self.selected_base.transfer_creatures(base)
            self.selected_base.set_selected()
            self.selected_base = None
        else:
            base.set_selected()
            self.selected_base = base

    def process_input(self, events):
        if events.mouse.l_clicked:
            for clickable in self.clickables:
                clickable.process_input(events)

    def update(self):
        for item in self.drawables:
            item.update()

        self.clickables = self.bases
        self.drawables = self.clickables
        self.ai.update()

    def draw(self, screen):
        screen.fill(NICE_BLUE)
        for drawable in self.drawables:
            drawable.draw(screen)


