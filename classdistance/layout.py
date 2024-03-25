import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
import tkinter.font as font
set_dpi_awareness()


class dist(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



        self.title("conv")

        container=ttk.Frame(self)
        container.grid(padx=60,pady=30,sticky="EW")
        
        
        frame=mtoft(container)
        frame.grid(row=0,column=0,sticky="NSEW")

        self.bind("<Return>",frame.calculate)
        self.bind("<KP_Enter>",frame.calculate)

class mtoft(ttk.Frame):
    def __init__(self,container,**kwargs):
        super().__init__(container,**kwargs)
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()
        metres_label = ttk.Label(self,text = "Metres: ")
        metres_input = ttk.Entry(self, width=10,textvariable=self.metres_value,font =("Segoe UI",15))
        feet_label = ttk.Label(self,text="feet: ")
        feet_display = ttk.Label(self,textvariable=self.feet_value)
        calc = ttk.Button(self, text="calculate",command=self.calculate)


        metres_label.grid(column=0,row=0,sticky="W")
        metres_input.grid(column=1,row=0,sticky="EW")
        metres_input.focus()
        feet_label.grid(column=0,row=1,sticky="W")
        feet_display.grid(column=1,row=1,sticky="EW")
        calc.grid(column=0,row=2,columnspan=2,sticky="EW")
   
        for child in self.winfo_children():
            child.grid_configure(padx=15,pady=15)
   
   
   
    def calculate(self,*args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            #print(f"{metres} metre is equal to {feet:.3f} feet.")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass

root=dist()
#root=tk.Tk()
font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)

root.mainloop()

