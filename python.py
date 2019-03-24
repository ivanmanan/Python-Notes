###############################################################################
# Installing Packages

# Installation is done for local user
# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

import numpy as np

###############################################################################
# Numbers

# Numbers without decimals is type int
# Numbers with decimal part is type float
# Division always returns floating point
# Operators with mixed type operands convert all integers to floating point
x = 2 + 2
x = 8 / 5
y = 3.55

# Floor division discards fractional result
x = 434 // 13
y = 434 % 13
print("Division is", x, "with remainder", y)

# ** calculates power
w = 7 ** 2

###############################################################################
# Strings

# Strings can be enclosed in '' or "" and both are same
# Backslash character \ can be used to escape quotes within strings
# Python strings are immutable and C++ strings are mutable
# C++: strings can be edited as an array of characters
# Python: strings must be reassigned a new value

# r before quotes indicate a raw string that ignores escape characters
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# Use triple quotes """...""" for strings to span multiple lines
# Note newline character is automatically added at the end of evrey line
# However, can add backslash \ at end of line to prevent newline character
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated with +
# Strings next to each other are concatenated automatically
# Note this only works with literals; variables require + sign
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
# Strings can be repeated with *
x = 3 * 'un' + 'ium'
print(x)
# Code below produces error because cannot do string and int operation
#x = 'hello' + 5

# Strings can be indexed
# Negative indices indicate starting from the right
word = 'Python'
print(word[0] + word[1] + word[-1])

# Slicing is used to obtain substring
word[0:2] # gives characters from position 0 (included) to position 2 (excluded)
word[:2] + word[2:] # gives entire array from start to 2, and 2 to end

# Returns the size of the string
len(word)

###############################################################################
# Lists
# Lists are mutable
squares = [1, 4, 9, 16, 25]
print(squares) # prints entire list
squares[0]  # indexing returns the item
squares[-1] # prints last element in list
squares[-3:]  # slicing returns a new list
# [9, 16, 25]

squares[:] # returns a new shallow copy of the list
squares + [36, 49, 64, 81, 100] # lsit concatenation

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # replace the wrong value
print(cubes)

# Replace parts of the list with splicing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
len(letters) # return size of list

###############################################################################
# Flow Control
# x = int(input("Please enter an integer: "))

# if x < 0:
#     print("Input is negative")
# elif x == 0:
#     print("Input is zero")
# else:
#     print("Input is positive")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# range function is used to iterate over a sequence of numbers
# prints 0-5
for i in range(5):
    print(i)

# prints 5-10
range(5, 10)
# prints 0, 3, 6, 9
range(0, 10, 3)
# prints -10, -40, -70
range(-10, -100, -30)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

###############################################################################
# Functions

# def means definition
def fib(n):    # write Fibonacci series up to n

    # Function's documentation or docstring
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, ' ')
        a, b = b, a+b
    print()

# Call the function
fib(2000)

# Renaming a function
f = fib
f(100)


###############################################################################
# Hash Tables

# Dictionary represents the implementation of a hash table
# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

###############################################################################
# Class

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# Instantiation of class uses function notation
x = MyClass()
print(x.i)
