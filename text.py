from const import *
import pygame
import pygame.gfxdraw

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



