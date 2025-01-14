# codewars

# 1) 
# This code does not execute properly. Try to figure out why.
# def multiply(a, b):
#     a * b

# correct code:

def multiply(a, b):
    return a * b

# 2)
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# 3)
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)

# 4)
# Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1]

# 5)
# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?

def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number
    
# 6)
# Very simple, given a number (integer / decimal / both depending on the language), 
# find its opposite (additive inverse).

def opposite(number):
    return number * -1

# 7)
# Complete the method that takes a boolean value and return a "Yes" string for true, 
# or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else: 
        return "No"
    
# 8)
# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    total = 0
    for x in arr:
        if x > 0:
            total += x
    return total

# 9)
# Write a function that accepts an integer n and a string s as parameters, 
# and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return repeat * string

# 10)
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. 
# You don't have to worry about strings with less than two characters.

def remove_char(s):
    return s[1:-1]

# 11)
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. 
# You don't have to worry about strings with less than two characters.

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num**2
    return total

# 12)
# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# 13)
# Note: This kata is inspired by Convert a Number to a String!. Try that one too.

def string_to_number(s):
    return int(s)

# 14)
# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0. 
# Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

def summation(num):
    return sum(range(1, num + 1))

# 15)
# Make a simple function called greet that returns the most-famous "hello world!".
# Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is a "hello world" solution you would want to show your friends?

def greet():
    return "hello world!"

# 16)
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    return sheep.count(True)

# 17)
# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2

# 18)
# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")

# 19)
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return f"Hello, {name} how are you doing today?"

# 20)
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

def boolean_to_string(b):
    return str(b)

# 21)
# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
# 22)
# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

def litres(time):
    return int(time * 0.5)

# 23)
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

def century(year):
    return (year + 99) // 100

# 24)
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    return [x * 2 for x in a]

# 25)
# Write a function that takes an array of numbers and returns the sum of the numbers. 
# The numbers can be negative or non-integer. 
# If the array does not contain any numbers then you should return 0.

def sum_array(a):
    return sum(a) if a else 0

# 26)
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

def paperwork(n, m):
    return max(0, n * m) if n >= 0 and m >= 0 else 0

# 27)
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()