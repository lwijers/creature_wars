"""
selection box class
returns all items by a selection box

api:
* load_selectables: takes a list with all clickable items, stores them
* give selection: returns selected items in a list

need to be called once a cycle:
* process input: takes all input (using own event pipeline), checks if relevenat input is used
* update: handles all the selecting
* draw: draws the box on the screen, takes the screen surface

if there are items in the selectable_items list it gets passed that you don't want to have selected
by the box, the items should have the box_selectable = False flag
"""

import pygame

class Selection_box():
    def __init__(self):
        self.selectables = []
        self.mouse_start = ()
        self.activated = False
        self.selection_made = False
        self.sel_rect = pygame.Rect(0,0,0,0)
        self.selection = []

        self.alpha = 100
        self.color = (200,200,200)


    def load_selectables(self, selectables):
        self.selectables = selectables

    def give_selection(self):
        # print(self.selection)
        return self.selection

    def process_input(self, events):
        self.selection = []
        if not self.activated:
            self.mouse_start = pygame.mouse.get_pos()

        if events.mouse.l_down:
            if pygame.mouse.get_rel() != (0, 0):
                self.activated = True

        if events.mouse.l_up:
            self.selection_made = True

    def update(self):
        if self.activated:
            self.sel_rect.topleft = (min(self.mouse_start[0], pygame.mouse.get_pos()[0]),
                                     min(self.mouse_start[1], pygame.mouse.get_pos()[1]))

            self.sel_rect.size = (abs(self.mouse_start[0] - pygame.mouse.get_pos()[0]),
                                  abs(self.mouse_start[1] - pygame.mouse.get_pos()[1]))

        if self.selection_made:
            for item in self.selectables:
                if item != self:
                    if self.sel_rect.colliderect(item.rect) and item.box_selectable:
                        self.selection.append(item)

            # self.give_selection()
            self.activated = False
            self.selection_made = False

    def draw(self, screen):
        selector = pygame.Surface(self.sel_rect.size)
        selector.set_alpha(self.alpha)
        selector.fill(self.color)
        selector.convert()
        if self.activated == True:
            pygame.draw.rect(selector, (150,150,150), pygame.Rect((0, 0), self.sel_rect.size), 2)
            screen.blit(selector, self.sel_rect)
