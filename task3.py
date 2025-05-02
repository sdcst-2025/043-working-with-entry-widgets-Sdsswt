#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

def calculate_add(event):
    calculate("+")

def calculate_sub(event):
    calculate("-")

def calculate_mul(event):
    calculate("*")

def calculate_div(event):
    calculate("/")

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = "Error" if num2 == 0 else num1 / num2

        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
        result_entry.config(state='disabled')
    except ValueError:
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid Input")
        result_entry.config(state='disabled')

w = tk.Tk()
w.geometry("400x300")
w.title("Number Calculator")

tk.Label(w, text="Number Calculator").grid(row=0, column=1, columnspan=2, pady=10)
tk.Label(w, text="Number 1").grid(row=1, column=0, padx=5)
tk.Label(w, text="Number 2").grid(row=1, column=3, padx=5)


entry1 = tk.Entry(w)
entry1.grid(row=2, column=0, padx=5, pady=5)

entry2 = tk.Entry(w)
entry2.grid(row=2, column=3, padx=5, pady=5)

result_entry = tk.Entry(w, state='disabled')
result_entry.place(x=130, y=150)


btn_add = tk.Button(w, text="+")
btn_add.grid(row=3, column=0)
btn_add.bind("<Button-1>", calculate_add)

btn_sub = tk.Button(w, text="-")
btn_sub.grid(row=3, column=1)
btn_sub.bind("<Button-1>", calculate_sub)

btn_mul = tk.Button(w, text="x")
btn_mul.grid(row=3, column=2)
btn_mul.bind("<Button-1>", calculate_mul)

btn_div = tk.Button(w, text="÷")
btn_div.grid(row=3, column=3)
btn_div.bind("<Button-1>", calculate_div)

w.mainloop()