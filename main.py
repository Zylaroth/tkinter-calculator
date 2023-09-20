import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Калькулятор")

display = tk.Entry(app, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

style = ttk.Style()
style.configure("TButton", padding=10, font=("Arial", 16))

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '+', '='
]

row_val = 1
col_val = 0

undo_stack = []

def on_button_click(value):
    current_text = display.get()
    if value == "=":
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Ошибка")
    elif value == "C":
        display.delete(0, tk.END)
    elif value == "Undo":
        if undo_stack:
            last_action = undo_stack.pop()
            display.delete(0, tk.END)
            display.insert(tk.END, last_action)
    else:
        display.insert(tk.END, value)
        undo_stack.append(current_text)

for button in buttons:
    ttk.Button(app, text=button, width=5, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ttk.Button(app, text="Undo", width=5, command=lambda: on_button_click("Undo")).grid(row=row_val, column=col_val)

app.mainloop()
