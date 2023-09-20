import tkinter as tk
from tkinter import ttk

def on_button_click(value):
    if value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Ошибка")
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)

app = tk.Tk()
app.title("Rалькулятор")

style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 16))

display = tk.Entry(app, width=20, font=("Helvetica", 20))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(app, text=button, width=5, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

app.mainloop()