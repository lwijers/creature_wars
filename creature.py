import pygame
from const import *
from vec2d import Vec2d
import asset_manager
import random


class Creature():
    def __init__(self, home, target):
        self.home = home
        self.target = target
        self.team = home.team
        self.x = random.randrange(self.home.hitbox.left, self.home.hitbox.right)
        self.y = self.home.hitbox.bottom-10
        self.w = 3
        self.h = 3
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.pos = Vec2d(self.rect.center)
        self.target_vec2d = Vec2d(target.rect.center)

        self.speed = 1

        self.image =  asset_manager.mngr.give_image('enemy_creature')

        if self.team == 'player':
            self.image = asset_manager.mngr.give_image('player_creature')

    def move(self):
        move = self.target_vec2d - self.pos
        move.length = self.speed
        self.pos += move
        self.rect.center = self.pos

    def kill(self):
        self.home.remove_creature(self)

    def update(self):
        self.move()
        if self.rect.colliderect(self.target.hitbox):
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.pos[0], self.pos[1]))
        # pygame.draw.rect(screen, self.bg_color, self.rect, 0)