from tkinter import *

class Radio():
    def __init__(self, master, texts, values, row, collumn,default='x'):
        self.options = []
        self.selected_option = StringVar(master,default)
        for x in range(len(texts)):
            key_config_radio = Radiobutton(master,variable=self.selected_option,text=texts[x],value=values[x])
            key_config_radio.grid(row=row+x,column=collumn)
            self.options.append(key_config_radio)
            
    
