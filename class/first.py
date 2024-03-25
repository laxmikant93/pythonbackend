import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()


class Helloworld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello")
        ttk.Label(self,text="hello").pack()
root=Helloworld()
root.mainloop()

