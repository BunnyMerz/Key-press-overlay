from PPlay.window import *
from key import *
from pad import *

def longest(double_list):
    biggest = 0
    for row in double_list:
        x = 0
        for col in row:
            x += 1
        if x > biggest:
            biggest = x
    return biggest



def keyboard_reader_main(config,pattern,symbols,keys,key_frame_file):
    key_frame = pygame.image.load(key_frame_file)
    kw = int(key_frame.get_width()/2)
    kh = key_frame.get_height()
    config['key_width'] = kw
    config['key_height'] = kh
    width = (longest(pattern) * (kw + int(config['margin_right']))) - int(config['margin_right'])
    height = (len(pattern) * (kh + int(config['margin_bottom']))) - int(config['margin_bottom'])

    window = Window(width,height)
    window.set_title("Keyboard reader")
    pygame.display.set_icon(pygame.image.load('cute_face.png'))
    window.set_background_color(eval(config['rgb']))
    clock = pygame.time.Clock()

    pad = Pad(keys, symbols, pattern, key_frame_file, config)

    pad.draw()

    while(True):
        pad.highlight()

        window.update()
        clock.tick(60)

config = {
    'rgb':[55, 239,0],
    'margin_right':0,
    'margin_bottom':0,
    'package_name':''
}

with open('main_config.txt','r') as main_config:
    for line in main_config:
        l = line.rstrip('\n').split('=')
        config[l[0]] = l[1]

with open('packages/' + config['package_name'] + '/config.txt','r') as package_config:
    symbols_keys = [{},{}]
    pattern = []
    z = 0
    for line in package_config:
        if z > 1:
            sys.exit('More then one empty line found in package config.txt')
        if line.strip('\n') == '':
            z += 1
        elif line[0] != '#': 
            l = (line.strip('\n').split('/'))
            if z == 0:
                symbols_keys[0][l[0]], symbols_keys[1][l[0]] = l[1],l[2]
            elif z == 1:
                for row in l:
                    pattern.append(row.split(' '))

symbols,keys = symbols_keys

# keyboard_reader_main(config,pattern,symbols,keys,'packages/tetris/key.png')