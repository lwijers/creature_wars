import pygame
import sys
import mouse
import keys

class Event_handler():
    def __init__(self):
        self.k_events = []
        self.m_events = []
        self.q_events = []

        self.mouse = mouse.Mouse()
        self.keyboard = keys.Keyboard()

        self.old_mouse_pos = (pygame.mouse.get_pos())
        self.counter = 0

    def event_handling(self):
        self.k_events = []
        self.m_events = []
        self.q_events = []

        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN or event.type is pygame.KEYUP:
                self.k_events.append(event)
            elif event.type is pygame.MOUSEBUTTONDOWN or event.type is pygame.MOUSEBUTTONUP:
                self.m_events.append(event)
            elif event.type is pygame.QUIT:
                self.q_events.append(event)

        self.mouse.handle_mouse(self.m_events)
        self.keyboard.handle_keys(self.k_events)

        self.check_exit(self.q_events)

    def check_exit(self, event):
        quit_attempt = False

        if event:
            quit_attempt = True

        for k1 in self.keyboard.keys_pressed:
            if k1.key == pygame.K_LALT or k1.key ==  pygame.K_RALT:
                for k2 in self.keyboard.keys_pressed:
                    if k2.key == pygame.K_F4:
                        quit_attempt = True


        if self.keyboard.key_down(pygame.K_ESCAPE):
            quit_attempt = True

        if quit_attempt:

            pygame.quit()
            sys.exit()
