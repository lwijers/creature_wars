import pygame
from const import *
from text import write
from const import *

class Powerbar():
    def __init__(self, x, y, bases):
        self.total_bases = bases
        self.player_creatures = 0
        self.enemy_creatures = 0
        self.w = SW - 100
        self.h = 20
        self.rect = pygame.Rect(x, y, self.w, self.h)
        self.rect.center = (SW/2, 950)
        self.enemy_width = 0

        self.enemy_color = RED
        self.player_color = GREEN

    def calculate_ratio(self):
        total_creatures = self.enemy_creatures + self.player_creatures
        creature_ratio = self.enemy_creatures / total_creatures
        enemy_bar = self.rect.width * creature_ratio
        self.enemy_width = enemy_bar

    def calculate_creatures(self):
        self.enemy_creatures = 0
        self.player_creatures = 0

        for base in self.total_bases:
            creatures = 0
            creatures += (len(base.released_creatures) + base.inhabitants)
            if base.team == 'enemy':
                self.enemy_creatures += creatures
            elif base.team == 'player':
                self.player_creatures += creatures

    def update(self):
        self.calculate_creatures()
        self.calculate_ratio()

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, RED, (self.rect.left, self.rect. top, self.enemy_width, self.rect.height))
        write(screen, self.enemy_creatures, self.rect.topleft)
        write(screen, self.player_creatures, self.rect.topright, right = True)