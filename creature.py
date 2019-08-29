import pygame
from const import *
from vec2d import Vec2d


class Creature():
    def __init__(self, home, target):
        self.home = home
        self.target = target
        self.team = home.team
        self.x = self.home.rect[0]
        self.y = self.home.rect[1]
        self.w = 3
        self.h = 3
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.pos = Vec2d(self.rect.center)
        self.target_vec2d = Vec2d(target.rect.center)

        self.speed = 1

        self.bg_color = RED

        if self.team == 'player':
            self.bg_color = GREEN

    def move(self):
        move = self.target_vec2d - self.pos
        move.length = self.speed
        self.pos += move
        self.rect.center = self.pos

    def kill(self):
        self.home.remove_creature(self)

    def update(self):
        self.move()
        if self.rect.colliderect(self.target.rect):
            self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, 0)