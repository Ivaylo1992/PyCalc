import tkinter as tk
from tkinter import messagebox


def on_digit_click(digit):
    current = display_var.get()
    display_var.set(current + str(digit))


def on_clear_click():
    display_var.set("")


def on_operation_click(operation):
    current = display_var.get()
    display_var.set(current + " " + operation + " ")


def on_equal_click():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
    except:
        messagebox.showerror('Error', 'Invalid expression')


root = tk.Tk()
root.title('PyCalc')
root.geometry('300x450')
root.configure(bg='#f2f2f2')

display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=('Arial', 18), justify='right', bd=8)
display_entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('**', 5, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 14))
    if text.isnumeric() or text == '.':
        button.config(command=lambda t=text: on_digit_click(t))
    elif text in '+-*/**()':
        button.config(command=lambda t=text: on_operation_click(t))
    else:
        button.config(command=on_equal_click)
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

clear_button = tk.Button(root, text='C', font=('Arial', 14), command=on_clear_click)
clear_button.grid(row=5, column=1, columnspan=4, padx=5, pady=5, ipadx=10, ipady=10)

root.mainloop()