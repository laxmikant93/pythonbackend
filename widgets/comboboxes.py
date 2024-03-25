import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

selected_weekdays = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekdays)
weekday['values']=("Monday","Tuesday","Wednesday","Thursday","Friday")
weekday["state"] = "readonly"
weekday.pack()

def handle_selection(event):
    print("today is", selected_weekdays.get())
    print("not available will be by friday")
    selected_weekdays.set("Friday")
    #print(weekday.current())
    print(selected_weekdays.get(), "was selected.")

weekday.bind("<<ComboboxSelected>>", handle_selection)


root.mainloop()

