import tkinter as tk
from tkinter import messagebox

def press(key):
    entry_text.set(entry_text.get() + str(key))

def clear():
    entry_text.set("")

def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")
        entry_text.set("")

def backspace():
    entry_text.set(entry_text.get()[:-1])

def inverse():
    try:
        value = float(entry_text.get())
        entry_text.set(str(-value))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def percentage():
    try:
        value = float(entry_text.get())
        result = value / 100 * float(previous_value.get()) if previous_value.get() else value / 100
        entry_text.set(str(result))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

root = tk.Tk()
root.title("Calculadora")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#2E2E2E")

entry_text = tk.StringVar()
previous_value = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 22), justify='right', bd=10, relief=tk.FLAT, bg="#1C1C1C", fg="white")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '⌫', '%', '±')
]

button_bg = "#3A3A3A"
button_fg = "white"
button_active_bg = "#505050"
button_font = ("Arial", 18)

def create_buttons():
    for row_values in buttons:
        row_frame = tk.Frame(root, bg="#2E2E2E")
        row_frame.pack(expand=True, fill=tk.BOTH)
        for value in row_values:
            if value == '=':
                button = tk.Button(row_frame, text=value, font=button_font, bg="#FF9500", fg="black", activebackground="#E08900", command=calculate)
            elif value == 'C':
                button = tk.Button(row_frame, text=value, font=button_font, bg="#D32F2F", fg="white", activebackground="#B71C1C", command=clear)
            elif value == '⌫':
                button = tk.Button(row_frame, text=value, font=button_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, command=backspace)
            elif value == '±':
                button = tk.Button(row_frame, text=value, font=button_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, command=inverse)
            elif value == '%':
                button = tk.Button(row_frame, text=value, font=button_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, command=percentage)
            else:
                button = tk.Button(row_frame, text=value, font=button_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, command=lambda v=value: [previous_value.set(entry_text.get()), press(v)])
            button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
            button.configure(relief=tk.FLAT, bd=5)

create_buttons()
root.mainloop()

