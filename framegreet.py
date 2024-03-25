import tkinter as tk
from tkinter import ttk

def greet():
    print(f"hello, {user_name.get() or 'world'}")

root = tk.Tk()

root.title("greeter")
user_name = tk.StringVar()
#ttk.Label(root, text="Hello",padding=(30, 10)).pack()
input_frame = ttk.Frame(root, padding=(20,10,20,0))
input_frame.pack(fill="both")
name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

buttons = ttk.Frame(root, padding=(20,10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()