# calculator

from tkinter import *

import parser

root = Tk()

root.title('Calculator')

# get the user input and place it in the textfield

i=0

def get_variable(num):
    global i
    display.insert(i, num)
    i += 1

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def calculate():
    entire_string= display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# adding the input field

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)


# adding buttons to the calculator

Button(root, text="1 ", bg="gray", command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2 ", bg="gray", command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3 ", bg="gray", command=lambda: get_variable(3)).grid(row=2, column=2)

Button(root, text="4 ", bg="gray", command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5 ", bg="gray", command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6 ", bg="gray", command=lambda: get_variable(6)).grid(row=3, column=2)

Button(root, text="7 ", bg="gray", command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8 ", bg="gray", command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9 ", bg="gray", command=lambda: get_variable(9)).grid(row=4, column=2)

# adding other buttons to the calculator

Button(root, text="C", bg="gray", fg="orange", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0 ", bg="gray", command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="=", bg="orange", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", bg="gray", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="- ", bg="gray", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="* ", bg="gray", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/ ", bg="gray", command=lambda: get_operation("/")).grid(row=5, column=3)

# addind new operations

Button(root, text="  pi ", bg="gray", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="  % ", bg="gray", command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="  (   ", bg="gray", command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", bg="gray", command=lambda: get_operation("**")).grid(row=5, column=4)

Button(root, text="AC", bg="gray", fg="orange", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="  .  ", bg="gray", command=lambda: get_operation(".")).grid(row=3, column=5)
Button(root, text="  )  ", bg="gray", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text=" ^2", bg="gray", command=lambda: get_operation("**2")).grid(row=5, column=5)


root.mainloop()


