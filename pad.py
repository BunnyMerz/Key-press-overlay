from PPlay.sprite import *
from key import *
import pygame

class Pad():
    def __init__(self, keys, symbols, pattern, key_frame, config, x=0, y=0):
        self.x = x
        self.y = y
        self.config = config

        self.pattern = pattern
        self.keys = {}
        self.build(keys,symbols,key_frame)
        self.align(x,y,pattern,self.keys)

    def build(self,keys,symbols,key_frame):
        for x in keys:
            self.keys[x] = (Key(keys[x],symbols[x],key_frame,self.config))

    def align(self,x,y,pattern,keys):
        xoff = 0
        yoff = 0
        width = int(self.config['key_width'])
        height = int(self.config['key_height'])
        margin_right = int(self.config['margin_right'])
        margin_bottom = int(self.config['margin_bottom'])
        z = 0
        for row in pattern:
            xoff = 0
            for collumn in row:
                if collumn != '0':
                    k = keys[collumn]
                    k.x = x + xoff
                    k.y = y + yoff
                    k.align()
                    z += 1
                    if z == len(keys):
                        return
                xoff += width + margin_right
            yoff += height + margin_bottom
    
    def draw(self):
        for x in self.keys:
            self.keys[x].draw()
    
    def highlight(self):
        for x in self.keys:
            self.keys[x].keydown()
