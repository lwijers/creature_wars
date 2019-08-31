import pygame
from const import *
from text import write
from const import *


class Powerbar():
    def __init__(self, x, y, bases):
        self.total_bases = bases  # list with all the bases in the level
        self.team_names = [] # list of strings, teamnames
        self.get_teamnames()
        self.team_colors = {}  # "team ": "teamcolor"
        self.get_team_colors()
        self.total_amount = 0  # holds the amount of all current creatures
        self.team_amounts = {}  # "team" : total amount creatures
        self.team_ratios = {}  # "team" : ratio of team tot total creatures
        self.team_rects = {}  # team : rect of that teams bar

        self.w = SW - 100
        self.h = 20
        self.rect = pygame.Rect(x, y, self.w, self.h)
        self.rect.center = (SW / 2, 950)

    def get_teamnames(self):
        for base in self.total_bases:
            if base.team not in self.team_names:
                self.team_names.append(base.team)

    def get_team_colors(self):
        for team in self.team_names:
            for base in self.total_bases:
                self.team_colors[base.team] = base.bg_color
        # print('team color', self.team_colors)

    def get_team_amounts(self):
        for team in self.team_names:
            self.team_amounts[team] = 0
            for base in self.total_bases:
                if base.team == team:
                    self.team_amounts[base.team] += len(base.released_creatures) + base.inhabitants
        # print('amounts', self.team_amounts)

    def get_total_amount(self):
        self.total_amount = 0
        for team in self.team_amounts:
            self.total_amount += self.team_amounts[team]
        # print(total', self.total_amount)


    def get_team_ratios(self):
        for team in self.team_names:
            self.team_ratios[team] = self.team_amounts[team] / self.total_amount
        # print('ratios', self.team_ratios)

    def create_bars(self):
        widths = 0  # holds the total width of the current counted bars
        for team in self.team_names:
            self.team_rects[team] = pygame.Rect(
                self.rect.left + widths,
                self.rect.top,
                self.rect.width * self.team_ratios[team],
                self.rect.height
            )
            widths += self.team_rects[team].width
        # print('bars', self.team_rects)

    def update(self):
        self.get_team_amounts()
        self.get_total_amount()
        self.get_team_ratios()
        self.create_bars()

    def draw(self, screen):
        for team in self.team_names:
            pygame.draw.rect(
                screen,
                self.team_colors[team],
                self.team_rects[team]
            )
            write(screen, self.team_amounts[team], self.team_rects[team].center, centered = True)

