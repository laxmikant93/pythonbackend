import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

language=("english","italian","french","spanish","portugese")
lang = tk.StringVar(value=language)
lang_select = tk.Listbox(root, listvariable=lang, height=6)
#lang_select["selectmode"] = "extended"
lang_select.pack()

#access the values
def handle_selection_change(event):
    selected_indices = lang_select.curselection()
    for i in selected_indices:
        print(lang_select.get(i))

lang_select.bind("<<ListboxSelect>>", handle_selection_change )
root.mainloop()

