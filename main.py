import tkinter as tk
from calculating import *

equation = []

def append_character(char):
    equation.append(char)
    print(equation)

def clear_equation():
    equation.clear()
    print(equation)

def backspace_equation():
    print(len(equation))
    if len(equation) > 0:
        equation.pop(len(equation) - 1)
    print(equation)

def calculate(equation):
    shunted_equation = shunting_algorithm(equation)
    print(evaluate_shunted_equation(shunted_equation))

# Creates window on screen
window = tk.Tk()

# Creates frames to hold the buttons and display
fr_display = tk.Frame()
fr_buttons = tk.Frame()

# Creates a textbox and places it on the display frame
tb_display = tk.Text(master=fr_display, width=29, height=5)
tb_display.pack()

# Creates all the buttons for the calculator and places them in a grid style on the buttons frame
# Operation buttons
btn_add = tk.Button(master=fr_buttons, text="+", width=7, height=3, command=lambda : append_character('+'))
btn_add.grid(column=3,row=0)
btn_minus = tk.Button(master=fr_buttons, text="-", width=7, height=3, command=lambda : append_character('-'))
btn_minus.grid(column=3,row=1)
btn_multiply = tk.Button(master=fr_buttons, text="*", width=7, height=3, command=lambda : append_character('*'))
btn_multiply.grid(column=3,row=2)
btn_divide = tk.Button(master=fr_buttons, text="/", width=7, height=3, command=lambda : append_character('/'))
btn_divide.grid(column=3,row=3)
btn_open_bracket = tk.Button(master=fr_buttons, text="(", width=7, height=3, command=lambda : append_character('('))
btn_open_bracket.grid(column=1,row=0)
btn_close_bracket = tk.Button(master=fr_buttons, text=")", width=7, height=3, command=lambda : append_character(')'))
btn_close_bracket.grid(column=2,row=0)
btn_equals = tk.Button(master=fr_buttons, text="=", width=7, height=3, command= lambda : calculate(equation)) # Calls func to solve equation
btn_equals.grid(column=3,row=4)

# Number buttons
btn_one = tk.Button(master=fr_buttons, text="1", width=7, height=3, command=lambda : append_character('1'))
btn_one.grid(column=0,row=3)
btn_two = tk.Button(master=fr_buttons, text="2", width=7, height=3, command=lambda : append_character('2'))
btn_two.grid(column=1,row=3)
btn_three = tk.Button(master=fr_buttons, text="3", width=7, height=3, command=lambda : append_character('3'))
btn_three.grid(column=2,row=3)
btn_four = tk.Button(master=fr_buttons, text="4", width=7, height=3, command=lambda : append_character('4'))
btn_four.grid(column=0,row=2)
btn_five = tk.Button(master=fr_buttons, text="5", width=7, height=3, command=lambda : append_character('5'))
btn_five.grid(column=1,row=2)
btn_six = tk.Button(master=fr_buttons, text="6", width=7, height=3, command=lambda : append_character('6'))
btn_six.grid(column=2,row=2)
btn_seven = tk.Button(master=fr_buttons, text="7", width=7, height=3, command=lambda : append_character('7'))
btn_seven.grid(column=0,row=1)
btn_eight = tk.Button(master=fr_buttons, text="8", width=7, height=3, command=lambda : append_character('8'))
btn_eight.grid(column=1,row=1)
btn_nine = tk.Button(master=fr_buttons, text="9", width=7, height=3, command=lambda : append_character('9'))
btn_nine.grid(column=2,row=1)
btn_zero = tk.Button(master=fr_buttons, text="0", width=7, height=3, command=lambda : append_character('0'))
btn_zero.grid(column=1,row=4)

# Other buttons
btn_dot = tk.Button(master=fr_buttons, text=".", width=7, height=3, command=lambda : append_character('.'))
btn_dot.grid(column=2,row=4)
btn_clr = tk.Button(master=fr_buttons, text="CLR", width=7, height=3, command=clear_equation) # Emptys equation list
btn_clr.grid(column=0,row=0)
btn_backspace = tk.Button(master=fr_buttons, text="DEL", width=7, height=3, command=backspace_equation) # Removes last character in equation list
btn_backspace.grid(column=0,row=4)

# Adds both frames onto the screen
fr_display.pack()
fr_buttons.pack()

# Halts the program to display the window
window.mainloop()

''' TODO: Add to github repo!!!!!
1. Make compatible with digitals over 9
2. Make compatible with decimals / floats
3. Make compatible with negative numbers
4. Add ^ button
5. Add ANS button to use the previous answer
'''