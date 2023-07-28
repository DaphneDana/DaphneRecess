# #day 3

# #basic operators and Expressions (input and output)
# # - Arithmetic operators
# # + Addition
# # - Subtraction
# # * multiplication
# # / division
# # // devide witout remainder
# # % moduluus
# # ** exponential

# # comparison operators
# #  == equal to
# #  != not equal to
# # > greater than 
# # < less than
# # >= greater than or equal to
# #  <= less than or equal to

# # Logical operators
# # logical AND 'and' 
# # logical OR 'or'
# # logical NOT 'not'


# # - Assignment operators
# # Asssign a value: '='
# # add value: '+'
# # Add and assign a value: '+='
# # Subtract and asssign a value: '-='
# # Divie and asssign a value: '/='
# # Modulus and assign a value: %=
# # exponantiate and assign a value: *=

# # -Membership operators
# #  In : 'in' operator: checks if a value exists in a sequence
# # not in: not in operator: checks if a value does not exist in a sequence

# # - Identity operators
# # Is: 'is' Checks if two values are the same
# # Is not: 'is not' operator: checks if two values are not the same

# ########################################################################
# # Examples
# ########################################################################

# # + Addition
# balls = 3 + 4
# print (balls)

# # - Subtraction
# y = 5000 - 30
# print(y)

# # * multiplication
# total  = 50000  * y
# print(total)

# # / division
# shares = 300 / 7
# print(shares)

# # // devide witout remainder
# a = 300  // 8
# print(a)

# # % moduluus
# rem = 10  % 4
# print(rem)

# # ** exponential
# e = 10 ** 2
# print(e)


# ################################################################################################

# # comparison operators
# a = 10
# b = 9
# #  == equal to
# if a == b:
#     print("a is equal to b")
#     print (a==b)
# #  != not equal to
# if a != b:
#     print("a is not equal to b")
#     print (a!=b)
# # > greater than 
# if a >b:
#     print("a is greater than b")
#     print (a>b)
# # < less than
# if a < b:
#     print("a is less than b")
#     print (a<b)
# # >= greater than or equal to
# if a >= b:
#     print("a is greater than or equal to b")
#     print (a>=b)
# #  <= less than or equal to
# if a <= b:
#     print("a is less than or equal to b")
#     print (a<=b)
    
# print(a == b)

# #######################################################################################
# #examples
# # Logical operators

# sunny = True
# windy = False
# # logical AND 'and' 
# if sunny and windy:
#     print('lets go play football')
# else:
#     print("it is bad weather")

# # logical OR 'or'
# if sunny or windy:
#     print("we can go fishing")
# else:
#     print('its a terrible weather')
# # logical NOT 'not'
# print (not windy)


# ################################################################

# # Assignment operators
# # compound assigment operators

# a = 5
# # add and assign
# a +=3
# print (a)

# #subtract and assign
# b = 10
# b -= 1
# print (b)

# # Divie and asssign a value: '/='

# c = 15
# c /= 3
# print (c)
# # Modulus and assign a value: %=

# d = 100
# d %= 7
# print (d)
# # exponantiate and assign a value: *=

# e = 2
# e *= 3
# print (e)

# #################################################################################


# # -Membership operators
# cars = ['BMW', 'Audi', 'Jeep', 'Rolls Royce']
# #  In : 'in' operator: checks if a value exists in a sequence
# if 'BMW' in cars:
#     print('BMW is in the list')
# else:
#     print('BMW is not in the list')
# # not in: not in operator: checks if a value does not exist in a sequence
# if 'Lexus' not in cars:
#     print('Lexus is in the list')
# else:
#     print('Lexus is not in the list')


# #####################################################################################
# # identity operators
# x = 'tall'
# y = 'tsll'
# print (x is y)
# print (x is not y)

# z = [1,2,3,4,5]
# w = [1,2,3,4,5]

# print(z is w)
# print (z is not w)


# ###################################################################################
# #Bitwise operator
# # are use to make operations on individual bits in binary numbers
# # bitwise AND '&' and Bitwise OR '|' operator
# # btwise XOR '^' 
# # Bitwise NOT '-' 
# # bitwise left shift '<<'
# # bitwise right shift '>>'


# # Examples of bitwise operations
# a = 10
# b = 20

# # bitwise AND '&' 
# print (a&b)

# # Bitwise OR '|' operator
# print (a|b)
# # btwise XOR '^' 
# print (a^b)
# # Bitwise NOT '-' 
# print(-a)
# # bitwise left shift '<<'
# print (a<<b)
# # bitwise right shift '>>
# print (a>>b)


# #############################################################################################
# # create a simple calculattor to add, subtract, multiply, and devide
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b

# def main():
#     print ('My first calculator')
#     number1 = float(input('Enter first number: '))
#     number2 =float( input('Enter second number: '))
#     operator = input("operator ('+, -, *, /) : ")
    
#     if operator == '+':
#         result = add(number1, number2)
#     elif operator == '-':
#         result = subtract(number1, number2)
#     elif operator == '*':
#         result = multiply(number1, number2)
#     elif operator == '/':
#         result = divide(number1, number2)
#     else:
#         print('Invalid operator')
    
#     print ('the result is ', result)
    
# if __name__ == '__main__':
#     main()
    
    
#     #  Assignmet 1: Create a simple calsculator program with a GUI.
#     # Make the title of your calcutor program window with your name eg Jeff Geof calculator

import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))


def button_clear():
    display.delete(0, tk.END)
#function called when equals signis pressed
def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
    display.delete(0, tk.END)
    display.insert(tk.END, result)

    

# Create the main window
window = tk.Tk()
window.title("Nakamyuka Daphne Simple Calculator")

# Create the display
display = tk.Entry(window, width=50, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=5, bg = "white", fg = "black", command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=5, bg ="white", fg = "black", command=lambda: button_click(0))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# Create the operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=5,  bg="#FFFDD0", fg="black", command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=5, bg="#FFFDD0", fg="black", command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=5, bg="#FFFDD0", fg="black", command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=5, bg="#FFFDD0", fg="black", command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=20, pady=5, bg="blue", fg="white", command=button_equal)
button_clear = tk.Button(window, text="C", padx=20, pady=5, bg="blue", fg="white", command=button_clear)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row=4, column=1)

# Run the main loop
window.mainloop()


