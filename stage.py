from const import *
import base
import ai
import random

class Stage():
    def __init__(self):

        self.selected_base = None

        self.types = ['player', 'enemy', 'neutral']
        self.amount = 100

        self.bases = [
            # base.Base(self, 40, 40, 'neutral', 30),
            # base.Base(self, 100, 110, 'player', 98),
            # base.Base(self, 40, 400, 'enemy', 20),
            # base.Base(self, 40, 600, 'neutral', 30),
            # base.Base(self, 300, 110, 'player', 98),

        ]

        for i in range (0, self.amount):
            self.bases.append(
                base.Base(
                    self,
                    random.randrange(20, 700),
                    random.randrange(20, 700),
                    random.choice(self.types),
                    random.randrange(20,100)
                )
            )


        self.clickables = self.bases
        self.drawables = self.clickables

        self.ai = ai.Ai(self)

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

        # for alarm in self.buildings[0].timer.alarms:
        #     print(
        #         self.buildings[0].timer.alarms[0].name,
        #         self.buildings[0].timer.alarms[0].current_time,
        #         self.buildings[0].timer.alarms[0].goal_time)

    def draw(self, screen):
        screen.fill(NICE_BLUE)
        for drawable in self.drawables:
            drawable.draw(screen)


