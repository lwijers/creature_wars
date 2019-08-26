import os

import pygame
import event_handler

import stage

os.environ['SDL_VIDEO_CENTERED'] = '0'

def run_game(width, height, fps):

    pygame.init()

    screen = pygame.display.set_mode( (100, 100))

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

        clock.tick( fps )


if __name__ == '__main__':
    run_game(100, 100, 60)