"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 

def run(e):
    data = e1Data.get()
    l1Data.set(data)
    e2Data.set(data)
    
win = tk.Tk()
win.geometry("500x500")

l1Data = tk.StringVar()
e1Data = tk.StringVar()
e2Data = tk.StringVar()
e2IntData = tk.IntVar()

lname1 = tk.Label(win,text="name")
lname1.place(x=90,y=50)
lname1.pack()

lname2 = tk.Label(win,text="student number")
lname2.place(x=90,y=50)
lname2.pack()

lname3 = tk.Label(win,text="grade")
lname3.place(x=90,y=50)
lname3.pack()

e1 = tk.Entry(win,width=15,textvariable=e1Data)
e1.pack()

e2 = tk.Entry(win,width=15,textvariable=e1Data)
e2.pack()

e3 = tk.Entry(win,width=15,textvariable=e1Data)
e3.pack()

e4 = tk.Entry(win, width=15, textvariable = e2Data)
e4.pack()

b1 = tk.Button(win,text="Click to display info")
b1.bind("<Button-1>",run)
b1.pack()

e1.place(x=50,y=50)
e2.place(x=200,y=50)
e3.place(x=350,y=50)
e4.place(x=50,y=200)
b1.place(x=50,y=100)
lname1.place(x=50,y=25)
lname2.place(x=200,y=25)
lname3.place(x=350,y=25)
win.mainloop()