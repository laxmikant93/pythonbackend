import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

def handle_scale(event):
    print(scale.get())
current_value = tk.DoubleVar()


scale = ttk.Scale(root, orient="horizontal",from_=0, to=10,command=handle_scale,variable=current_value)
scale.pack(fill="x")

scale["state"] = "normal"
root.mainloop()

print(current_value.get())