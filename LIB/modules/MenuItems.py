# -*- coding: utf-8 -*-
import Globals, pygame
from GlobalFuncs import change_color_alpha
from TransparentText import AlphaText

class MenuItem():
    def __init__(self, text, type, group, number=None):
        self.type = type
        self.text = AlphaText(text, group, number)
        self.init_for_group(group)
    def init_for_group(self, group):
        self.tooltip = None
        if group[:4] == 'main':
            self.active_zone = self.text.rect.inflate(500-self.text.rect.w, 0)
    def render(self, highlighted_menuitem):
        if self.text.AV:
            self.text.render()
class Cursor():
    def __init__(self, menuitems, type):
        self.surf_color = change_color_alpha(Globals.COLORS['black'], 0)
        self.init_for_type(type)
        rects = [menuitems[key].text.rect for key in self.keys]
        self.y_cords = [rect.y-3 for rect in rects]
        self.size = (500, rects[0].h+6)
        self.x = rects[0].x-(self.size[0]-rects[0].w)/2
        self.change_pos(self.keys[0])
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)
    def init_for_type(self, type):
        if type == 'main_main':
            self.keys = ['new_game', 'settings', 'stats', 'exit']
            self.u_colors = ['green200', 'yellow', 'yellow', 'red']
    def change_pos(self, key):
        self.active = self.keys.index(key)
        self.y = self.y_cords[self.active]
        self.u_length = -13
    def render(self):
        if self.u_length != self.size[0]/2-3:
            self.u_length += 20
            if self.surf_color.a != 104:
                self.surf_color.a += 8
            pygame.draw.rect(self.surf, self.surf_color, pygame.Rect((0, 0), self.size), 0)
            pygame.draw.line(self.surf, Globals.COLORS[self.u_colors[self.active]], (self.size[0]/2-self.u_length, self.size[1]-1), (self.size[0]/2+self.u_length, self.size[1]-1), 1)
        Globals.screen.blit(self.surf, (self.x, self.y))
