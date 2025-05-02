"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 

def run(event):
    name = name_var.get()
    student_number = student_number_var.get()
    grade = grade_var.get()
    
    result = f"Name: {name}, Student #: {student_number}, Grade: {grade}"
    result_var.set(result)

win = tk.Tk()
win.geometry("500x300")

name_var = tk.StringVar()
student_number_var = tk.StringVar()
grade_var = tk.StringVar()
result_var = tk.StringVar()


tk.Label(win, text="Name").place(x=50, y=20)
tk.Label(win, text="Student Number").place(x=200, y=20)
tk.Label(win, text="Grade").place(x=370, y=20)


e1 = tk.Entry(win, width=15, textvariable=name_var)
e2 = tk.Entry(win, width=15, textvariable=student_number_var)
e3 = tk.Entry(win, width=15, textvariable=grade_var)
e4 = tk.Entry(win, width=50, textvariable=result_var, state='readonly')

e1.place(x=50, y=50)
e2.place(x=200, y=50)
e3.place(x=370, y=50)
e4.place(x=50, y=150)


b1 = tk.Button(win, text="Click to display info")
b1.bind("<Button-1>", run)
b1.place(x=50, y=100)

win.mainloop()