# Code Wars

# 1)
# task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
#     else:
#         raise ValueError("Invalid operator")

# 2)
# The first century spans from the year 1 up to and including the year 100, 
# the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# def century(year):
#     return (year + 99) // 100

# 3)
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

# def count_sheeps(sheep):
#     return sheep.count(True)

# 4)
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# def string_to_number(s):
#     return int(s)

# 5)
# The task is to invert the values in a given list, changing each value to its negative counterpart.

# def invert(lst):
#     return [-x for x in lst]

# 6)
# Write a function which calculates the average of the numbers in a given list.

# 7)
# def find_average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)

# 8)
# Let's play! You have to return which player won! In case of a draw return

# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif (p1 == "rock" and p2 == "scissors") or \
#          (p1 == "scissors" and p2 == "paper") or \
#          (p1 == "paper" and p2 == "rock"):
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"

# 9)
# Given a non-empty array of integers, return the result of multiplying the values together in order

# def grow(arr):
#     result = 1
#     for num in arr:
#         result *= num
#     return result

# 10)
# It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.

# def get_average(marks):
#     return sum(marks) // len(marks)

# 11)
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

# def greet(name):
#     return f"Hello, {name} how are you doing today?"

# 12)
# Complete the function so that it finds the average of 
# the three scores passed to it and returns the letter value associated with that grade.

# def get_grade(s1, s2, s3):
#     avg = (s1 + s2 + s3) / 3
#     if avg >= 90:
#         return 'A'
#     elif avg >= 80:
#         return 'B'
#     elif avg >= 70:
#         return 'C'
#     elif avg >= 60:
#         return 'D'
#     else:
#         return 'F'