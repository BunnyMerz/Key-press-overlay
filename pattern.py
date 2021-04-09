from tkinter import *

class Pattern():
    def __init__(self, master):
        self.width = IntVar(master,'1')
        self.height = IntVar(master,'1')
        self.pattern = [[StringVar(master)]]
        self.entry_grid = []
        self.master = master

        self.entry_frame = Frame(master,name="entry_frame")
        self.entry_frame.grid(row=1,column=0)

        self.width_entry = Entry(master,text='width',textvariable=self.width,width=3)
        self.height_entry = Entry(master,text='height',textvariable=self.height,width=3)

        self.width_entry.grid(row=0,column=1)
        Label(master,text=" x ").grid(row=0,column=2)
        self.height_entry.grid(row=0,column=3)

        bt = Button(master,text='Update with new size', command = self.double_grid)
        bt.grid(row=0,column=4)

        self.double_grid()

    def double_grid(self):
        ## There is a bug with using the build_grid() once
        ## To replicate: Change the column or widht value (for eg, from 1x1 to 2x2) and fill the new squares. Now click on 'update with new size' again. All new values will be gone
        self.build_grid()
        self.build_grid()

    def build_grid(self):
        difference = self.width.get() - len(self.pattern[0])
        if difference > 0:
            for rows in self.pattern:
                for x in range(difference):
                    rows.append(StringVar(self.master))
        elif difference < 0:
            for rows in range(len(self.pattern)):
                self.pattern[rows] = self.pattern[rows][:difference]
            
        difference = self.height.get() - len(self.pattern)
        if difference > 0:
            for x in range(difference):
                row_ah = []
                for z in range(self.width.get()):
                    row_ah.append(StringVar(self.master))
                self.pattern.append(row_ah)
        elif difference < 0:
            self.pattern = self.pattern[:difference]
        
        self.build_entry_fields()

    def build_entry_fields(self):
        self.entry_frame.destroy()
        self.entry_frame = Frame(self.master,name="entry_frame")
        self.entry_frame.grid(row=1,column=0)
        self.entry_grid = self.pattern
        
        for y in range(self.height.get()):
            for x in range(self.width.get()):
                self.entry_grid[y][x] = Entry(self.entry_frame,name=str(y) + "x" + str(x),width=3,textvariable=self.pattern[y][x])
                self.entry_grid[y][x].grid(column=x,row=y)
    
    def get_values(self):
        values = []
        for rows in self.pattern:
            values_rows = []
            for col in rows:
                values_rows.append(col.get())
            values.append(values_rows)
        return values



