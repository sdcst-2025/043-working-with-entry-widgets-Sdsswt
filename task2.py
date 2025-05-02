#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
import math

def run(event):
    try:
        a = float(side1.get())
        b = float(side2.get())
        hypotenuse = calculate_hypotenuse(a, b)
        result.set(f"Hypotenuse: {round(hypotenuse, 2)}")
    except ValueError:
        result.set("Invalid input")

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


win = tk.Tk()
win.geometry("500x300")
win.title("Hypotenuse Calculator")


side1 = tk.StringVar()
side2 = tk.StringVar()
result = tk.StringVar()


tk.Label(win, text="Side 1").place(x=50, y=20)
tk.Label(win, text="Side 2").place(x=200, y=20)


e1 = tk.Entry(win, width=15, textvariable=side1)
e2 = tk.Entry(win, width=15, textvariable=side2)
e4 = tk.Entry(win, width=50, textvariable=result, state='readonly')

e1.place(x=50, y=50)
e2.place(x=200, y=50)
e4.place(x=50, y=150)


b1 = tk.Button(win, text="Click to calculate")
b1.bind("<Button-1>", run)
b1.place(x=50, y=100)

win.mainloop()