import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

image = Image.open("widgets/logo.png").resize((64,64))
photo= ImageTk.PhotoImage(image)

label= ttk.Label(root,image=photo,padding=5)
#label.config(font=("segoe ui",20))
label.pack()


root.mainloop()