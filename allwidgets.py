###widgets and tools/formula
#import tkinter as tk

#win = tk.Tk()
#win.title("My Window")
#win.geometry("400x300")
#win.mainloop()

#Label	tk.Label(win, text="Hello")	Display text
#Button	tk.Button(win, text="Click me", command=function)	Button for actions
#Entry	tk.Entry(win)	Input text field
#Text	tk.Text(win)	Multi-line text area
#Checkbutton	tk.Checkbutton(win, text="Option")	Checkbox
#Radiobutton	tk.Radiobutton(win, text="Choice 1", value=1)	Select one option
#Listbox	tk.Listbox(win)	List selection
#Scale	tk.Scale(win, from_=0, to=100)	Slider control
#Spinbox	tk.Spinbox(win, from_=0, to=10)	Up/down number selection
#Messagebox (popup)	tk.messagebox.showinfo("Title", "Message")	Show popup window
#Canvas	tk.Canvas(win, width=200, height=100)	Draw shapes, images
#Frame	tk.Frame(win)	Container to group widgets
# Widget Placement

#Method	Syntax	Behavior
#pack()	widget.pack()	Stack widgets vertically or horizontally
#grid()	widget.grid(row=0, column=0)	Place widgets in a table layout
#place()	widget.place(x=100, y=50)	Absolute position
# Useful Formulas and Tools

#Task	How to do it
#Get text from Entry	text = entry.get()
#Set text in Entry	entry.insert(0, "hello")
#Clear Entry	entry.delete(0, tk.END)
#Bind Button to event	button.bind("<Button-1>", function)
#Change Entry to readonly	Entry(state='readonly')
#Update Label dynamically	label.config(text="New Text")
#StringVar for dynamic text	
#- Create:	var = tk.StringVar()
#- Assign to widget:	Entry(textvariable=var) or Label(textvariable=var)
#- Set value:	var.set("New Value")
#- Get value:	value = var.get()
# Simple Example Putting It Together
#python
#Copy
#Edit

#import tkinter as tk

#def greet():
    #name = entry.get()
    #result.set(f"Hello, {name}!")

#win = tk.Tk()
#win.title("Simple Greeting App")
#win.geometry("300x200")

#tk.Label(win, text="Enter your name:").pack(pady=5)
#entry = tk.Entry(win)
#entry.pack(pady=5)

#result = tk.StringVar()
#tk.Entry(win, textvariable=result, state="readonly").pack(pady=5)

#btn = tk.Button(win, text="Greet", command=greet)
#btn.pack(pady=5)

#win.mainloop()

import tkinter as tk
import math

# ----------------- Main Logic -------------------
help_visible = False  # Toggle state for help box

def factor(event=None):
    try:
        a = int(a_input.get())
        b = int(b_input.get())
        c = int(c_input.get())

        discriminant = b**2 - 4*a*c
        advanced = choice_var.get() == "Advanced"

        if discriminant >= 0:
            sqrt_d = math.sqrt(discriminant)
            root1 = (-b + sqrt_d) / (2 * a)
            root2 = (-b - sqrt_d) / (2 * a)

            r1 = int(root1) if root1.is_integer() else round(root1, 2)
            r2 = int(root2) if root2.is_integer() else round(root2, 2)
            factored = f"(x - {r1})(x - {r2})"

            if advanced:
                factored += f"  |  D={discriminant}, Roots: {r1}, {r2}"

        else:
            real = round(-b / (2 * a), 2)
            imag = round(math.sqrt(-discriminant) / (2 * a), 2)
            factored = f"(x - ({real} + {imag}i))(x - ({real} - {imag}i))"

            if advanced:
                factored += f"  |  D={discriminant}, Roots: Complex"

        result.set(factored)
        update_listbox(factored)

    except:
        result.set("Invalid input")

def reset_inputs():
    a_input.delete(0, tk.END)
    b_input.delete(0, tk.END)
    c_input.delete(0, tk.END)
    result.set("")
    help_text.delete("1.0", tk.END)
    help_button.config(text="Show Help")
    global help_visible
    help_visible = False

def show_help():
    global help_visible
    if not help_visible:
        help_text.delete("1.0", tk.END)
        help_text.insert(tk.END,
            "Help:\n"
            "- Enter integer values for a, b, and c.\n"
            "- Click 'Factor Trinomial' to calculate.\n"
            "- Works for real and complex roots.\n"
            "- Use 'Advanced Mode' to show extra info.\n"
            "- Results are saved to history.\n"
            "- 'Reset' clears all inputs and result.")
        help_visible = True
        help_button.config(text="Hide Help")
    else:
        help_text.delete("1.0", tk.END)
        help_visible = False
        help_button.config(text="Show Help")

def update_label(val):
    scale_label.config(text=f"Scale Value: {val}")

def update_listbox(factored_text):
    listbox.insert(tk.END, factored_text)

# ----------------- GUI Setup -------------------
win = tk.Tk()
win.title("Trinomial Factoring Tool")
win.geometry("570x540")
win.resizable(False, False)

# -------- Input Frame --------
frame = tk.LabelFrame(win, text="Input Coefficients", padx=10, pady=10)
frame.place(x=20, y=10, width=530, height=120)

tk.Label(frame, text="a:").grid(row=0, column=0, padx=10, pady=5)
a_input = tk.Entry(frame, width=5)
a_input.grid(row=0, column=1)

tk.Label(frame, text="b:").grid(row=0, column=2, padx=10)
b_input = tk.Entry(frame, width=5)
b_input.grid(row=0, column=3)

tk.Label(frame, text="c:").grid(row=0, column=4, padx=10)
c_input = tk.Entry(frame, width=5)
c_input.grid(row=0, column=5)

# -------- Buttons --------
btn_factor = tk.Button(win, text="Factor Trinomial", width=18, command=factor)
btn_factor.place(x=50, y=140)

btn_reset = tk.Button(win, text="Reset", width=10, command=reset_inputs)
btn_reset.place(x=220, y=140)

help_button = tk.Button(win, text="Show Help", width=12, command=show_help)
help_button.place(x=330, y=140)

# -------- Result Output --------
tk.Label(win, text="Factored Form:").place(x=50, y=185)
result = tk.StringVar()
output = tk.Entry(win, width=55, textvariable=result, state="readonly")
output.place(x=50, y=210)

# -------- History Listbox --------
tk.Label(win, text="History:").place(x=50, y=245)
listbox = tk.Listbox(win, width=55, height=5)
listbox.place(x=50, y=265)

# -------- Mode & Scale --------
choice_var = tk.StringVar(value="Normal")
tk.Label(win, text="Mode:").place(x=50, y=370)
tk.Radiobutton(win, text="Normal", variable=choice_var, value="Normal").place(x=100, y=370)
tk.Radiobutton(win, text="Advanced", variable=choice_var, value="Advanced").place(x=180, y=370)

scale_label = tk.Label(win, text="Scale Value: 0")
scale_label.place(x=330, y=340)

scale = tk.Scale(win, from_=0, to=10, orient="horizontal", command=update_label)
scale.place(x=300, y=370)

# -------- Canvas Decoration --------
canvas = tk.Canvas(win, width=100, height=50, bg="lightblue")
canvas.place(x=430, y=20)
canvas.create_text(50, 25, text="ax² + bx + c", font=("Arial", 10, "bold"))

# -------- Help Box --------
help_text = tk.Text(win, width=66, height=5, wrap="word")
help_text.place(x=20, y=430)

win.mainloop()