import os

import pygame
import event_handler
from const import *

import stage

# os.environ['SDL_VIDEO_CENTERED'] = '0'
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1400,10)
def run_game(width, height, fps):

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    e_handler = event_handler.Event_handler()
    s = stage.Stage()

    running = True

    while running:

        e_handler.event_handling()

        s.process_input(e_handler)

        s.update()

        s.draw(screen)

        pygame.display.flip()

        clock.tick( 60 )


if __name__ == '__main__':
    run_game(SW, SH, FPS)