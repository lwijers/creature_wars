''' ---spygmae2d_versieIII---, created by Lennart on 3/6/2018'''
import pygame


class Mouse():
    def __init__(self):
        self.l_down = False
        self.l_up = True
        self.l_clicked = False

        self.m_down = False
        self.m_up = True
        self.m_clicked = False

        self.r_down = False
        self.r_up = True
        self.r_clicked = False
        self.wheel_up = False
        self.wheel_down = False


    def reset_buttons(self):
        self.l_clicked = False
        self.m_clicked = False
        self.r_clicked = False


    def handle_mouse(self, events):
        self.reset_buttons()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.l_down = True
                self.l_up = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.l_down = False
                self.l_up = True
                self.l_clicked = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.r_down = True
                self.r_up = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.r_down = False
                self.r_up = True
                self.r_clicked = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                self.m_down= True
                self.m_up = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                self.m_down = False
                self.m_up = True
                self.m_clicked = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                self.wheel_up = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 5:
                self.wheel_down = True
