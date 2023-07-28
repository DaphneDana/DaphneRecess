import os
# Exception handling

# devided by 0
x = int(input('Num1: '))
y = int(input('Num2: '))


def divide(x, y):
    return x / y


try:
    print(divide(x, y))

except ZeroDivisionError:
    print('Cannot divide by zero')

# type error
x = 3
y = 'i am fine'
try:
    z = y + x
except TypeError:
    print('cannot add an integer to a string')


# index error for index out of range
cars = ['buatti', 'BMW', 'Audi']
try:
    print(cars[1])
    print(cars[3])
except IndexError:
    print('index out of range')


# name error

try:
    print(name)
except:
    print('parameter not defined')


# KeyError
students = {
    'james': 50,
    'John': 74,
    'Jennifer': 65
}
try:
    marks = students['Junior']
    print(marks)
except KeyError:
    print("Could not findkey in dictionary")

# Using finally and else in exception handling

n1 = int(input('Num1: '))
n2 = int(input('Num2: '))
try:
    sum = n1/n2
except Exception:
    print('An error occurred')
else:
    print('No error occured')
finally:
    print('this is always executed')

##########################################################################
# File Handlling
# we use open to create a file
# it takes two parameters wc include
# -the file name and mode
# r- opens for reading and returns an error if file does not exist
# -a - opens file for appending and creates one if it does not exist
# -w - opens file for writing and creates one if it does not exist
# x - creates a specified file and returns an error if it already exists


# open a file
file1 = open('file.txt', 'w')


# write to a file
file1.write('First line in this file \n')
file1.write('second line in this file\n')


# closing the file
file1.close()

# read from a file
f = open('file.txt', 'r')
print(f.read())

f.close()

# appending to the file

fo = open('file.txt', 'a')
fo.write('i have appended this')

fo.close()

# read contents again
fr = open('file.txt', 'r')
print(fr.read())

fr.close()

# deleting a file

# os.remove('file.txt')
