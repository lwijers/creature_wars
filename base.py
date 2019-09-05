import pygame
from const import *
from text import write
import creature
import timer
import asset_manager

class Base:

    def __init__(self, stage, x, y, team, inhabitants):
        self.stage = stage
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.hitbox = pygame.Rect(self.x, self.y, self.w - 50, self.h - 30)
        self.hitbox.midbottom = self.rect.midbottom

        self.team = team

        self.bg_color = RED
        self.image = asset_manager.mngr.give_image('enemy_base')

        if self.team == 'player':
            self.bg_color = GREEN
            self.image = asset_manager.mngr.give_image('player_base')

        elif self.team == 'neutral':
            self.bg_color = DARK_GREY
            self.image = asset_manager.mngr.give_image('neutral_base')

        # else:
        #     self.bg_color = RED




        self.selected = False

        self.timer = timer.Timer()

        self.inhabitants = inhabitants
        self.max_inhabitants = 100
        self.inhabitants_growth_speed = 1
        self.inhabitants_decay = 0.98

        self.timer.set_alarm('inhabitants_grow', self.inhabitants_growth_speed)

        self.transfer_amount = 10 # creatures released per click
        self.to_transfer_amount = 0 # creatures yet to transfer
        self.in_transfer_amount = 0 # creatures base has in transfer
        self.creature_release_time = 0.5  # interval between releasing

        self.time_to_release = False  # if the interval has passed
        self.currently_releasing = False  # if currently releasing creatures
        self.released_creatures = []  # all released creatures

        self.box_selectable = False # if it gets picked up by the selection box
        if self.team == 'player':
            self.box_selectable = True


    def set_selected(self):
        self.selected =not self.selected

    def add_creature(self, home, target):
        self.released_creatures.append(creature.Creature(home, target))

    def add_inhabitant(self):
        self.inhabitants += 1

    def remove_inhabitant(self):
        self.inhabitants -= 1

    def remove_creature(self, creature):
        if creature.team == creature.target.team:
            creature.target.add_inhabitant()
        else:
            creature.target.remove_inhabitant()
            creature.target.check_capture(creature.team)

        self.released_creatures.remove(creature)
        self.in_transfer_amount -= 1

    def transfer_creatures(self, base):
        if self.inhabitants > 1 :
            self.currently_releasing = True
            self.target_base = base
            self.to_transfer_amount += self.transfer_amount
            self.timer.set_alarm("creature_release_time", self.creature_release_time)

    def regulate_growth(self):
        if self.timer.check_alarm('inhabitants_grow'):
            if self.inhabitants < self.max_inhabitants:
                if self.team != 'neutral':
                    self.inhabitants += 1

            else:
                buffer = int(self.inhabitants * self.inhabitants_decay)
                if buffer < 100:
                    buffer = 100
                self.inhabitants = buffer

    def check_departures(self):
        if self.currently_releasing:
            if self.timer.check_alarm("creature_release_time"):
                self.time_to_release = True
                if self.inhabitants > 1: # if the base has more than 1 inhabitant
                    self.add_creature(self, self.target_base) # spawn creature
                    self.to_transfer_amount -= 1
                    self.inhabitants -= 1
                    self.in_transfer_amount += 1
                else:
                    self.time_to_release = False
                    self.timer.remove_alarm("creature_release_time")
                    self.to_transfer_amount = 0

        if self.to_transfer_amount <= 0:
            self.timer.remove_alarm("creature_release_time")
            self.currently_releasing = False

    def check_capture(self, enemy_team):
        if self.inhabitants < 0:
            self.team = enemy_team
            self.image = asset_manager.mngr.give_image(enemy_team + '_base')
            self.inhabitants += 2
            if self.team == 'player':
                self.bg_color = GREEN
            else:
                self.bg_color = RED

    # PUD ---------------------------------------------------------------------------

    def process_input(self, events):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if events.mouse.l_clicked:
                    self.stage.select_building(self)

            elif events.mouse.r_clicked:
                self.stage.upgrade_wheel.switch_active(self)

    def update(self):
        for item in self.released_creatures:
            item.update()
        self.timer.update()
        self.check_departures()
        self.regulate_growth()

    def draw(self, screen):
        screen.blit(self.image, (self.rect))
        # pygame.draw.rect(screen, self.bg_color, self.rect, 0)
        if self.selected:
            pygame.draw.rect(screen, WHITE, self.rect, 3)
        write(screen, self.inhabitants, (self.rect.center), centered=True)

        # write(screen, "team: {}".format(self.team),
        #       (self.rect.right + 5, self.rect.top), font_cat = 'std_small' )
        # write(screen, "to transfer: {}".format(self.to_transfer_amount),
        #       (self.rect.right + 5, self.rect.top + 10 ), font_cat='std_small')
        # write(screen, "in transfer: {}".format(self.in_transfer_amount),
        #       (self.rect.right + 5, self.rect.top + 20), font_cat='std_small')


        for creature in self.released_creatures:
            creature.draw(screen)
