import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Rалькулятор")

display = tk.Entry(app, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

style = ttk.Style()
style.configure("TButton", padding=10, font=("Arial", 16))

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(app, text=button, width=5).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

app.mainloop()