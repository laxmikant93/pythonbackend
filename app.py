import tkinter as tk
from tkinter import ttk

def greet():
    print("hello world!!")

root = tk.Tk()
#ttk.Label(root, text="Hello",padding=(30, 10)).pack()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand="true")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()