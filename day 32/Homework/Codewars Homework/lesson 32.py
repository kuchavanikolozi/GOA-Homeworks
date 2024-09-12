# codewars

# 1) Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

def opposite(number):
    return -number

# 2) Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else: 
        return "No"
    
# 3) Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return repeat * string

# 4) Make a simple function called greet that returns the most-famous "hello world!".

def greet():
    return "hello world!"

# 5)
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2