from tkinter import *

class Checkbox():
    def __init__(self, master, texts, row, collumn, default='x'):
        self.options = []
        self.options_vars = []
        for x in range(len(texts)):
            on_off = IntVar(master,0)
            key_config_radio = Checkbutton(master, variable=on_off, onvalue=1, offvalue=0, text=texts[x])
            key_config_radio.grid(row=row+x,column=collumn)
            self.options.append(key_config_radio)
            self.options_vars.append(on_off)
            
    def get_bools(self):
        return self.options_vars
    
    def gray_out(self,indexes):
        for i in indexes:
            self.options[i].config(state='normal')
    
    def ungray_out(self,indexes):
        for i in indexes:
            self.options[i].config(state='disabled')
            self.options[i].deselect()
    
    def gray_setup(self,gray_list):
        for x in range(len(gray_list)):
            if gray_list[x] == 0:
                self.options[x].config(state="disabled")
                self.options[x].deselect()
            elif gray_list[x] == 1:
                self.options[x].config(state='normal')

    def reset_gray(self):
        return
