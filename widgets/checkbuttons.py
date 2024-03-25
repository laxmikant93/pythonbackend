import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

#check_buttons = ttk.Checkbutton(root,text="check me!")
#check_buttons.pack()
selected_options= tk.StringVar()

def print_current_option():
    print(selected_options.get())
check = ttk.Checkbutton(
root,
text="check example",
variable=selected_options,
command=print_current_option,
onvalue="yes",
offvalue="no")

check.pack()
root.mainloop()