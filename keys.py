''' ---spygmae2d_versieIII---, created by Lennart on 3/6/2018'''
import pygame

class Keyboard():
    def __init__(self):
        self.keys_pressed = []
        self.k_down = False
        self.k_up = False

    def handle_keys(self, events):
        self.k_down = False
        self.k_up = False

        try:
            for event in events:
                if event.type is pygame.KEYDOWN:
                    self.keys_pressed.append(event)
                    self.k_down = event

                if event.type is pygame.KEYUP:
                    self.k_up = event
                    self.keys_pressed.remove(event)

        except ValueError:
            pass

    def key_down(self, key_to_check):
        if self.k_down and self.k_down.key is key_to_check:
            return True

        else:
             return False