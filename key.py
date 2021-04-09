from PPlay.sprite import *
import pygame
import win32api

keychart = {
    'left':37,
    'up':38,
    'right':39,
    'down':40,
    'space_bar':32,
    'l_shift':160,
    'r_shift':161
}

class Key():
    "Classe que possui o frame e o symbol"
    def __init__(self, key, symbol, key_frame,config):
        self.x = 0
        self.y = 0

        try:
            self.key = keychart[key]
        except:
            self.key = ord(key.upper())

        self.frame = Sprite(key_frame, 2)
        self.symbol = Sprite('packages/' + config['package_name'] +'/' +  symbol, 1)
        self.state = 0

        self.align()
    
    def press(self):
        self.frame.curr_frame = 0
        self.state = 1

    def unpress(self):
        self.frame.curr_frame = 1
        self.state = 0
    
    def keydown(self):
        if (win32api.GetKeyState((self.key)) & (1 << 7)) != 0:
            if self.state == 0:
                self.draw()
            self.press()
        else:
            if self.state == 1:
                self.draw()
            self.unpress()

    def align(self):
        self.frame.x, self.frame.y = self.x, self.y
        self.symbol.x, self.symbol.y = self.x, self.y

    def draw(self):
        self.frame.draw()
        self.symbol.draw()
