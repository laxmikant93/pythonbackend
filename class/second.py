import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()



class inputframe(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="enter name: ")
        entry = ttk.Entry(self,textvariable=self.user_input)
        button = ttk.Button(self,command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")
    
    def greet(self):
        print(f"hello, {self.user_input.get()}!")

root=tk.Tk()


frame = inputframe(root)

#label.pack()
frame.pack()
root.mainloop()

