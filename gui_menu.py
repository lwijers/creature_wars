from const import *
import pygame
import pygame.gfxdraw

class Menu():
    def __init__(self):

        self.w = 300
        self.h = SH
        self.rect = pygame.Rect((0,0, self.w, self.h))
        self.rect.topright = (SW, 0)

        self.bg_color = WHITE

        self.clickables = []
        self.clickables.append(Radio_button(self, "Start",  (10,10), label_change = "Stop"))
        self.drawables = self.clickables


    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


    def process_input(self, events):
        for item in self.clickables:
            item.process_input(events)

    def update(self):
        pass

    def draw(self, screen):

        pygame.draw.rect(screen, self.bg_color, self.rect, 0)
        for item in self.drawables:
            item.draw(screen)


class Radio_button():
    def __init__(self, parent, label, pos, rad=10,
                 border_color=BLACK, color=WHITE,
                 active_color=GREEN,
                 label_change = False
                 ):
        self.label = label
        self.start_label = label

        self.parent = parent
        self.pos = pos
        self.rad = rad
        #TODO make the position relevant to parent surface not screen
        self.rect = pygame.Rect(0,0, self.rad *2, self.rad * 2)
        self.rect.left = self.parent.rect.left + self.pos[0]
        self.rect.top = self.parent.rect.top + self.pos[1]


        self.border_color = border_color
        self.color = color
        self.active_color = active_color
        self.current_color = self.color
        self.activated = False


        self.label_change = label_change

    def process_input(self, events):
        if events.mouse.l_clicked and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.activated:
                self.current_color = self.color
                self.activated = False
                if self.label_change:
                    self.label = self.label_change

            else:
                self.current_color = self.active_color
                self.activated = True
                if self.label_change:
                    self.label = self.start_label

    def update(self):
        pass

    def draw(self, screen):
        pygame.gfxdraw.filled_circle(
            screen,
            self.parent.rect.left + self.pos[0] + self.rad,
            self.parent.rect.top + self.pos[1] + self.rad,
            self.rad, self.border_color
        )

        pygame.gfxdraw.filled_circle(
            screen,
            self.parent.rect.left + self.pos[0] + self.rad,
            self.parent.rect.top + self.pos[1] + self.rad,
            self.rad - 4, self.current_color
        )
        write(screen, self.label, (self.rect.right+self.rad, self.rect.top ))


ui_fonts = {
    'std':      {'type': 'Century Gothic',
                'size': 30,
                'color': WHITE
            },
    'std_small' :{'type': 'Century Gothic',
                 'size': 17,
               'color': YELLOW
            },
    'std_white':{'type': 'Century Gothic',
                'size': 12,
                'color': BLUE
            },
    'hdr': {'type': 'Calibri',
                'size': 30,
                'color': YELLOW
            },
}

def write(surface, text, pos, font_cat = 'std', color=False, centered = False, right=False):
    pygame.font.init()
    my_font = pygame.font.SysFont(ui_fonts[font_cat]['type'], ui_fonts[font_cat]['size'])
    my_text = str(text)

    if color == False:
        my_label = my_font.render(my_text, 1, ui_fonts[font_cat]['color'])
    else:
        my_label = my_font.render(my_text, 1, color)

    if centered == True:
        surface.blit(my_label, (pos[0] - my_label.get_width() / 2,
                                pos[1]- my_label.get_height() / 2 + 1))

    elif right == True:
        surface.blit(my_label, (pos[0] - my_label.get_width(),
                                pos[1]
                                ))
    else:
        surface.blit(my_label, (pos[0], pos[1]))
        return



