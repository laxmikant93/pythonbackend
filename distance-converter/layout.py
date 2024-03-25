import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
import tkinter.font as font
set_dpi_awareness()

root=tk.Tk()
root.title("Distance converter")
font.nametofont("TkDefaultFont").configure(size=15)



metres_value = tk.StringVar()
feet_value = tk.StringVar()

def calculate(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        #print(f"{metres} metre is equal to {feet:.3f} feet.")
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

root.columnconfigure(0, weight=1)
main=ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main,text = "Metres: ")
metres_input = ttk.Entry(main, width=10,textvariable=metres_value,font =("Segoe UI",15))
feet_label = ttk.Label(main,text="feet: ")
feet_display = ttk.Label(main,textvariable=feet_value)
calc = ttk.Button(main, text="calculate",command=calculate)

metres_label.grid(column=0,row=0,sticky="W")
metres_input.grid(column=1,row=0,sticky="EW")
metres_input.focus()
feet_label.grid(column=0,row=1,sticky="W")
feet_display.grid(column=1,row=1,sticky="EW")
calc.grid(column=0,row=2,columnspan=2,sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15,pady=15)


root.bind("<Return>",calculate)
root.bind("<KP_Enter>",calculate)

root.mainloop()

