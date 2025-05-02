"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
import math

win = tk.Tk()
win.title("Trinomial Factoring")
win.geometry("400x260")

def factor(event=None):
    try:
        a = int(a_input.get())
        b = int(b_input.get())
        c = int(c_input.get())

        discriminant = b**2 - 4*a*c

        if discriminant >= 0:
            sqrt_d = math.sqrt(discriminant)
            root1 = (-b + sqrt_d) / (2*a)
            root2 = (-b - sqrt_d) / (2*a)

            root1 = int(root1) if root1.is_integer() else round(root1, 2)
            root2 = int(root2) if root2.is_integer() else round(root2, 2)

            if root1 >= 0:
                factored = (f"(x - ({root1} + {root2}))"
                        f"(x - ({root1} - {root2}))")
            elif root1 < 0:
                factored = (f"(x + ({root1} + {root2}))"
                        f"(x + ({root1} - {root2}))")

            factored = f"(x - ({root1}))(x - ({root2}))"
        else:
            f1 = round(-b / (2*a), 2)
            f2 = round(math.sqrt(-discriminant) / (2*a), 2)
        
            if f1 >= 0:
                factored = (f"(x - ({f1} + {f2}))"
                        f"(x - ({f1} - {f2}))")
            elif f1 < 0:
                factored = (f"(x + ({f1} + {f2}))"
                        f"(x + ({f1} - {f2}))")

        result.set(factored)
    except:
        result.set("Invalid input")

def reset_inputs():
    a_input.delete(0, tk.END)
    b_input.delete(0, tk.END)
    c_input.delete(0, tk.END)
    result.set("")

# --------------------------------------------------------------------------------

tk.Label(win, text="Enter coefficients for: ax² + bx + c").place(x=100, y=10)

tk.Label(win, text="a:").place(x=50, y=50)
a_input = tk.Entry(win, width=6)
a_input.place(x=80, y=50)

tk.Label(win, text="b:").place(x=150, y=50)
b_input = tk.Entry(win, width=6)
b_input.place(x=180, y=50)

tk.Label(win, text="c:").place(x=250, y=50)
c_input = tk.Entry(win, width=6)
c_input.place(x=280, y=50)

btn = tk.Button(win, text="Factor Trinomial")
btn.bind("<Button-1>", factor)
btn.place(x=100, y=100)

reset_button = tk.Button(win, text="Reset", command=reset_inputs)
reset_button.place(x=220, y=100)

result = tk.StringVar()
output = tk.Entry(win, width=40, textvariable=result, state="readonly")
output.place(x=50, y=170)

win.mainloop()