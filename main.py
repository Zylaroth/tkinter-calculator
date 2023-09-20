import tkinter as tk

app = tk.Tk()
app.title("TEST")

display = tk.Entry(app, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

app.mainloop()
