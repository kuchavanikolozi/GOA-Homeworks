#1) We need to Write the sintax that prints Hello World!
#  print("Hello World!")

#2) We need Create an script that takes user input and prints it.

# user_input = int(input("Please input any number: "))
# print("Thanks.")

# 3) We need to Write a script that uses both single-line and multi-line comments.

# The input() function prompts the user for input and stores it in the variable 'user_input'.

# user_input = input("Please input something: ")
# print("Thank you.")

# This is a multi-line comment.
# It explains that the following lines of code
# will print the user input to the screen.
# Multi-line comments are useful for providing
# detailed explanations or documentation.

# 4) Write a script that demonstrates indentation in Python.

# Define a function to greet the user based on the time of day.
# def greet_user():
#     # Ask the user to input the time of day.
#     time_of_day = input("What time of day is it (morning, afternoon,or evening)? ")

#     # Conditional statements to determine the appropriate greeting.
#     if time_of_day == "morning":
#         # Print a greeting for the morning.
#         print("Good morning!")
#     elif time_of_day == "afternoon":
#         # Print a greeting for the afternoon.
#         print("Good afternoon!")
#     elif time_of_day == "evening":
#         # Print a greeting for the evening.
#         print("Good evening!")
#     else:
#         # Print a message if the input does not match any of the expected values.
#         print("Hello!")
# greet_user()

#5) 
# long_string = "This is a very long string " \
#               "that is broken into two lines " \
#               "for better readability."

# print(long_string)

#6) We need to Write a script and use comments to explain a function's purpose

# def add(a, b):
#     return a + b  # Return the sum

# print(add(2, 3))  

# 7) Use comments to disable a part of the script and re-enable it
# print("This line is disabled and won't run")

print("This line is enabled and will run")

# 8) Write a script with intentional errors and comment on why they occur
# This script has intentional errors

# Missing closing parenthesis
# print("Hello, World!"  

# Incorrect indentation
# if True:
# print("Indented incorrectly")

# Incorrect variable name
# number = 10
# print(Number)  # 'Number' is not defined, should be 'number'

# 9) Create and initialize multiple variables of different data types

# integer = 5
# float = 15.5
# string = "Hello, world!"
# boolean = True

# print(integer, float, string, boolean)

# 10) Swap the values of two variables

# a = 12
# b = 14

# Swapping
# a, b = b, a

# print("a:", a)
# print("b:", b)

# 11) Create a script that takes user input to assign values to variables

# name = input("Please input your name: ")
# age = int(input("Please input your age: "))

# print("Name:", name)
# print("Age:", age)

# 12) Demonstrate variable naming conventions in Python.

#  Snake Case
# user_name = "Nika"
# total_price = 134

#  Camel Case
# userName = "Alice"
# totalPrice = 103

# 13) Create variables of types: integer, float, string, and boolean.

# Integer
# age = 25

# Float
# height = 5.9

# String
# name = "Alice"

# Boolean
# is_student = True

# 14) Write a script to convert between different data types.

# 15) Demonstrate the use of type() function to check variable types.
# age = 15
# height = 1,48
# name = "Nika"
# is_student = ("Student of goa" True)

# print(type(age))  # <class 'int'>
# print(type(height))  # <class 'float'>
# print(type(name))  # <class 'str'>
# print(type(is_student))  # <class 'bool'>

# Arithmetic operations with integers and floats
# sum_result = age + height  # 25 + 5.9 = 30.9
# diff_result = age - height  # 25 - 5.9 = 19.1
# product_result = age * height  # 25 * 5.9 = 147.5
# division_result = age / height  # 25 / 5.9 ≈ 4.24

#  Concatenating strings
# full_name = name + "Kuchava"  # "Nikolozi" + "Kuchava" = "Nikolozi Kuchava"

# Boolean operations
# is_adult = age >= 18  # True

# 16) Write a script to compare different data types using relational operators.

#  Comparing integers and floats
# print(age > height)  # 25 > 5.9 -> True
# print(age == 25)  # 25 == 25 -> True
# print(age != 30)  # 25 != 30 -> True

# Comparing strings
# print(name == "Nikolozi")  # "Nikolozi" == "Nikolozi" -> True
# print(name != "Giorgi")  # "Nikolozi" != "Giorgi" -> True

# Comparing boolean values
# print(is_student == True)  # True == True -> True
# print(is_student == False)  # True == False -> False

# 17) 
# Basic arithmetic operations
# a = 15
# b = 4

# Addition
# add_result = a + b  # 15 + 4 = 19

# Subtraction
# subtract_result = a - b  # 15 - 4 = 11

# # Multiplication
# multiply_result = a * b  # 15 * 4 = 60

# Division
# divide_result = a / b  # 15 / 4 = 3.75

# Modulus (remainder of division)
# modulus_result = a % b  # 15 % 4 = 3

# Exponentiation (power)
# power_result = a ** b  # 15^4 = 50625

# Floor Division
# floor_division_result = a // b  # 15 // 4 = 3

# print("Addition: " (add_result))
# print("Subtraction:" (subtract_result))
# print("Multiplication: "(multiply_result))
# print("Division: " (divide_result))
# print("Modulus: " (modulus_result))
# print("Power: " (power_result))
# print("Floor Division: " (floor_division_result))

# 18)Write a script to perform arithmetic operations.

# Function to perform arithmetic operations

# Step 1: Import the random module
# import random

# Step 2: Generate a random floating-point number between 0 and 100
# random_float = random.uniform(0, 100)

# Step 3: Print the random number
# print("The random floating-point number is:", random_float)

# 19)Write a script that calculates the square root of a number.
# Step 1: Import the math module
# import math

# Step 2: Define a number
# number = 16  # You can change this number to any positive value

# Step 3: Calculate the square root of the number
# square_root = math.sqrt(number)

# Step 4: Print the result
# print("The square root of", number, "is:", square_root)

# 20)Demonstrate the use of math functions like ceil() and floor().
# Step 1: Import the math module

# import math

# Step 2: Define a floating-point number
# number = 4.7  # You can change this number to any floating-point value

# Step 3: Calculate the ceiling value of the number
# ceiling_value = math.ceil(number)

# Step 4: Calculate the floor value of the number
# floor_value = math.floor(number)

# Step 5: Print the results
# print("The ceiling value of", number, "is:", ceiling_value)
# print("The floor value of", number, "is:", floor_value)

# 21)Write a script to find the greatest common divisor (GCD) of two numbers.

# 22)Write a script to convert integers to floats and vice versa.

# Step 1: Define an integer
# integer_value = 5  # You can change this number to any integer value

# Step 2: Convert the integer to a float
# float_value_from_integer = float(integer_value)

# Step 3: Define a float
# float_value = 7.8  # You can change this number to any float value

# Step 4: Convert the float to an integer
# integer_value_from_float = int(float_value)

# Step 5: Print the results
# print("Original integer:", integer_value)
# print("Converted to float:", float_value_from_integer)

# print("Original float:", float_value)
# print("Converted to integer:", integer_value_from_float)

# 23)Create a script to convert strings to integers and floats.

# Step 1: Define a string representing an integer
# string_integer = "42"

# Step 2: Convert the string to an integer
# integer_value = int(string_integer)

# Step 3: Define a string representing a float
# string_float = "3.14"

# Step 4: Convert the string to a float
# float_value = float(string_float)

# Step 5: Print the results
# print("String as integer:", integer_value)
# print("String as float:", float_value)

# 24)Demonstrate casting between lists and tuples.

# Step 1: Define a list
# list_value = [1, 2, 3, 4, 5]

# Step 2: Convert the list to a tuple
# tuple_from_list = tuple(list_value)

# Step 3: Define a tuple
# tuple_value = (6, 7, 8, 9, 10)

# Step 4: Convert the tuple to a list
# list_from_tuple = list(tuple_value)

# Step 5: Print the results
# print("List:", list_value)
# print("Converted to tuple:", tuple_from_list)

# print("Tuple:", tuple_value)
# print("Converted to list:", list_from_tuple)

# Create a script to convert a string representing a number to an integer.

# Step 1: Define a string representing a number
# number_string = "123"

# Step 2: Convert the string to an integer
# number_integer = int(number_string)

# Step 3: Print the result
# print("String as integer:", number_integer)

# 25) Write a script to demonstrate the use of boolean values.
# Step 1: Define some boolean values
# is_sunny = True
# is_raining = False

# Step 2: Print the boolean values
# print("Is it sunny?", is_sunny)
# print("Is it raining?", is_raining)

# 26)Create a script to perform logical operations (and, or, not).
# Step 1: Define some boolean values
# a = True
# b = False

# Step 2: Perform logical operations
# and_result = a and b
# or_result = a or b
# not_result_a = not a
# not_result_b = not b

# Step 3: Print the results
# print("a and b:", and_result)
# print("a or b:", or_result)
# print("not a:", not_result_a)
# print("not b:", not_result_b)

# 27)Demonstrate the use of comparison operators to return boolean values.

# Step 1: Define some variables
# x = 10
# y = 20

# Step 2: Perform comparisons
# is_equal = (x == y)
# is_not_equal = (x != y)
# is_greater = (x > y)
# is_less = (x < y)
# is_greater_or_equal = (x >= y)
# is_less_or_equal = (x <= y)

# Step 3: Print the results
# print("x == y:", is_equal)
# print("x != y:", is_not_equal)
# print("x > y:", is_greater)
# print("x < y:", is_less)
# print("x >= y:", is_greater_or_equal)
# print("x <= y:", is_less_or_equal)

# 28)Write a script that uses if-else statements based on boolean values.
# Step 1: Define a boolean value
# is_logged_in = True

# Step 2: Use if-else statements based on the boolean value
# if is_logged_in:
#     print("Welcome back, user!")
# else:
#     print("Please log in to continue.")

# 29)Create a script that returns a boolean result from a function.

# Step 1: Define a function that returns a boolean value
# def is_even(number):
#     return number % 2 == 0

# Step 2: Test the function
# test_number = 42
# result = is_even(test_number)

# Step 3: Print the result
# print(f"Is {test_number} even? {result}")
 
# 30)Demonstrate the use of comparison operators to return boolean values.

# Step 1: Define some variables
# x = 10
# y = 20

# Step 2: Perform comparisons
# is_equal = (x == y)
# is_not_equal = (x != y)
# is_greater = (x > y)
# is_less = (x < y)
# is_greater_or_equal = (x >= y)
# is_less_or_equal = (x <= y)

# Step 3: Print the results
# print("x == y:", is_equal)
# print("x != y:", is_not_equal)
# print("x > y:", is_greater)
# print("x < y:", is_less)
# print("x >= y:", is_greater_or_equal)
# print("x <= y:", is_less_or_equal)

# 31) Write a script that uses if-else statements based on boolean values.
# Define a boolean variable to represent if it is raining
# is_raining = True 

# Use an if-else statement to make a decision based on the value of is_raining
# if is_raining:
#     print("It is raining. Take an umbrella.")
# else:
#     print("It is not raining. Wear sunglasses.")

# 32) Create a script that returns a boolean result from a function.
# def is_adult(age):
#     # This function checks if a given age qualifies as an adult.
#     # :param age: The age to check
#     # :return: True if the age is 18 or older, False otherwise
#     if age >= 18:
#         return True
#     else:
#         return False

# age_to_check = 20
# result = is_adult(age_to_check)
# print(f"Is the person with age {age_to_check} an adult? {result}")

# 33) Write a script that demonstrates arithmetic operators.
# Define two numbers to perform arithmetic operations
# num1 = 15
# num2 = 3

# Addition
# addition = num1 + num2
# print(f"{num1} + {num2} = {addition}")

# Subtraction
# subtraction = num1 - num2
# print(f"{num1} - {num2} = {subtraction}")

# Multiplication
# multiplication = num1 * num2
# print(f"{num1} * {num2} = {multiplication}")

# Division
# division = num1 / num2
# print(f"{num1} / {num2} = {division}")

# Modulus (remainder of division)
# modulus = num1 % num2
# print(f"{num1} % {num2} = {modulus}")

# Exponentiation (num1 raised to the power of num2)
# exponentiation = num1 ** num2
# print(f"{num1} ** {num2} = {exponentiation}")

# Floor division (division without the remainder)
# floor_division = num1 // num2
# print(f"{num1} // {num2} = {floor_division}")

# 34) Create a script to use assignment operators.

# Initial value
# number = 10

# Assignment with addition
# number += 5  # equivalent to number = number + 5
# print(f"After addition assignment, number = {number}")

# Assignment with subtraction
# number -= 3  # equivalent to number = number - 3
# print(f"After subtraction assignment, number = {number}")

# Assignment with multiplication
# number *= 2  # equivalent to number = number * 2
# print(f"After multiplication assignment, number = {number}")

# Assignment with division
# number /= 4  # equivalent to number = number / 4
# print(f"After division assignment, number = {number}")

# Assignment with modulus
# number %= 3  # equivalent to number = number % 3
# print(f"After modulus assignment, number = {number}")

# Assignment with exponentiation
# number **= 2  # equivalent to number = number ** 2
# print(f"After exponentiation assignment, number = {number}")

# Assignment with floor division
# number //= 2  # equivalent to number = number // 2
# print(f"After floor division assignment, number = {number}")

# 35) Write a script to show the use of comparison operators.

# Define two numbers
# a = 15
# b = 10

# Equal to
# print(f"Is {a} equal to {b}? {a == b}")

# Not equal to
# print(f"Is {a} not equal to {b}? {a != b}")

# Greater than
# print(f"Is {a} greater than {b}? {a > b}")

# Less than
# print(f"Is {a} less than {b}? {a < b}")

# Greater than or equal to
# print(f"Is {a} greater than or equal to {b}? {a >= b}")

# Less than or equal to
# print(f"Is {a} less than or equal to {b}? {a <= b}")

# 36) Demonstrate the use of logical operators in a script.
# Define boolean variables
# x = True
# y = False

# Logical AND
# print(f"{x} AND {y} is {x and y}")

# Logical OR
# print(f"{x} OR {y} is {x or y}")

# Logical NOT
# print(f"NOT {x} is {not x}")
# print(f"NOT {y} is {not y}")

# Combining logical operators
# print(f"({x} AND {y}) OR {x} is {(x and y) or x}")
# print(f"({x} OR {y}) AND {not y} is {(x or y) and not y}")

# 37) Create a script to use identity operators (is, is not).

# Define some variables
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# d = a.copy()

# Identity operator 'is'
# print(f"a is b: {a is b}")  # True, because b is a reference to a
# print(f"a is c: {a is c}")  # False, because c is a different list object
# print(f"a is d: {a is d}")  # False, because d is a copy of a

# Identity operator 'is not'
# print(f"a is not b: {a is not b}")  # False, because b is a reference to a
# print(f"a is not c: {a is not c}")  # True, because c is a different list object
# print(f"a is not d: {a is not d}")  # True, because d is a copy of a

# 38) Write a script to create and print a list.

# Create a list of fruits
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the list
# print("List of fruits:", fruits)

# 39)Create a script to add and remove elements from a list.

# Create a list of fruits
# fruits = ["apple", "banana", "cherry"]

# Add elements to the list
# fruits.append("date")  # Add to the end
# print("After appending 'date':", fruits)

# fruits.insert(1, "blueberry")  # Add at specific index
# print("After inserting 'blueberry' at index 1:", fruits)

# Remove elements from the list
# fruits.remove("banana")  # Remove by value
# print("After removing 'banana':", fruits)

# removed_fruit = fruits.pop(2)  # Remove by index
# print(f"After popping element at index 2 ({removed_fruit}):", fruits)

# Clear the entire list
# fruits.clear()
# print("After clearing the list:", fruits)

# 40) Write a script to sort a list.
# Create a list of numbers
# numbers = [4, 2, 9, 1, 5, 6]

# Sort the list in ascending order
# numbers.sort()
# print("List sorted in ascending order:", numbers)

# Sort the list in descending order
# numbers.sort(reverse=True)
# print("List sorted in descending order:", numbers)

# Sorting a list of strings
# words = ["banana", "apple", "cherry", "date"]
# words.sort()
# print("List of words sorted in alphabetical order:", words)

# 41) Demonstrate the use of list comprehension.
# Create a list of numbers
# numbers = [1, 2, 3, 4, 5]

# Use list comprehension to create a list of squares
# squares = [x**2 for x in numbers]
# print("List of squares:", squares)

# Use list comprehension with a condition
# even_squares = [x**2 for x in numbers if x % 2 == 0]
# print("List of squares of even numbers:", even_squares)

# Create a list of strings and use list comprehension to convert to uppercase
# words = ["hello", "world", "python"]
# uppercase_words = [word.upper() for word in words]
# print("List of uppercase words:", uppercase_words)

# 42)Create a script to find the length of a list.
# Create a list of fruits
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Find and print the length of the list
# length_of_fruits = len(fruits)
# print("Length of the list of fruits:", length_of_fruits)

# 43) Write a script that uses an if statement to check a condition.
# Define a variable
# number = 10

# Use an if statement to check a condition
# if number > 5:
#     print(f"The number {number} is greater than 5.")

# 44) Create a script that uses an if-else statement.
# Define a variable
# number = 3

# Use an if-else statement to check a condition
# if number > 5:
#     print(f"The number {number} is greater than 5.")
# else:
#     print(f"The number {number} is not greater than 5.")

# 45) Write a script that uses an if-elif-else statement.

# Define a variable
# number = 7

# Use an if-elif-else statement to check multiple conditions
# if number > 10:
#     print(f"The number {number} is greater than 10.")
# elif number > 5:
#     print(f"The number {number} is greater than 5 but less than or equal to 10.")
# else:
#     print(f"The number {number} is 5 or less.")

# 46) Demonstrate nested if statements.
# Define a variable
# number = 8

# Use nested if statements to check multiple conditions
# if number > 5:
#     print(f"The number {number} is greater than 5.")
#     if number % 2 == 0:
#         print(f"The number {number} is also even.")
#     else:
#         print(f"The number {number} is odd.")
# else:
#     print(f"The number {number} is 5 or less.")

# 47) Write a script that uses the ternary operator.

# Define a variable
# number = 9

# Use the ternary operator to check a condition and assign a value
# result = "greater than 5" if number > 5 else "5 or less"
# print(f"The number {number} is {result}.")

# 48) Write a script to demonstrate a while loop.
# Initialize a counter variable
# count = 0

# Use a while loop to iterate until the condition is false
# while count < 5:
#     print(f"Count is {count}")
#     count += 1  # Increment the counter

# print("While loop ended.")

# 49) Create a script that uses a while loop with a break statement.
# Initialize a counter variable
# count = 0

# Use a while loop with a break statement
# while count < 10:
#     if count == 5:
#         print("Breaking out of the loop.")
#         break  # Exit the loop when count is 5
#     print(f"Count is {count}")
#     count += 1

# print("While loop ended.")

# 50) Write a script that uses a while loop with a continue statement.

# Initialize a counter variable
# count = 0

# Use a while loop with a continue statement
# while count < 10:
#     count += 1  # Increment the counter
#     if count % 2 == 0:
#         continue  # Skip the rest of the loop when count is even
#     print(f"Count is {count}")

# print("While loop ended.")

# 51) Demonstrate an infinite loop and how to stop it.
# import time

# # Demonstrate an infinite loop
# try:
#     while True:
#         print("This is an infinite loop. Press Ctrl+C to stop.")
#         time.sleep(1)  # Sleep for 1 second to slow down the output
# except KeyboardInterrupt:
#     print("Infinite loop stopped by user.")

# 52) Create a script that uses a while loop to iterate over a list.

# Define a list of fruits
# fruits = ["apple", "banana", "cherry", "date"]

# Initialize an index variable
# index = 0

# # Use a while loop to iterate over the list
# while index < len(fruits):
#     print(f"Fruit at index {index} is {fruits[index]}")
#     index += 1  # Move to the next index

# print("While loop ended.")

# 53) Write a script to demonstrate a for loop.
# for i in range (11):
#     print(i)

# 54) Create a script that uses a for loop to iterate over a list.
# Define a list of fruits
# fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
# for fruit in fruits:
#     print(f"Fruit: {fruit}")

# print("For loop ended.")

# 55) Write a script that uses a for loop with the range() function.
# Use a for loop with the range() function to iterate a specific number of times
# for i in range(1, 6):  # range(start, stop) - iterates from 1 to 5
#     print(i)

# Use a for loop with the range() function and a step value
# for i in range(0, 10, 2):  # range(start, stop, step) - iterates with a step of 2
#     print(i)

# print("For loop ended.")

# 56)Demonstrate nested for loops.
# Demonstrate nested for loops
# for i in range(3):  # Outer loop
#     for j in range(2):  # Inner loop
#         print(i,j)

# print("Nested for loops ended.")

# 57) Create a script that uses a for loop with an else clause.
# Define a list of numbers
# numbers = [1, 2, 3, 4, 5]

# Use a for loop with an else clause
# for number in numbers:
#     print(number)
# else:
#     # This block is executed after the for loop completes normally
#     print("For loop completed without encountering a break.")

# Example with a break to show the else clause being skipped
# for number in numbers:
#     if number == 3:
#         break  # Exit the loop
#     print(number)
# else:
#     print("For loop completed without encountering a break.")  # This won't be executed if break is encountered

# print("For loop with else ended.")

# 58) Write a script to define and call a function.

# Define a function
# def greet():
#     print("Hello, world!")

# Call the function
# greet()

# 59) Create a script that uses a function with parameters.

# Define a function with parameters
# def greet(name, age):
#     print(f"Hello, {name}! You are {age} years old.")

# Call the function with arguments
# greet("Nika", 15)
# greet("Luka", 22)

# 60)Write a script that uses a function with a return value.

# Define a function that returns a value
# def add_numbers(a, b):
#     return a + b

# Call the function and store the result
# result = add_numbers(10, 5)
# print(result)

# 61) Demonstrate the use of default parameters in a function.
# Define a function with default parameters
# def greet(name="Nikolozi", greeting="Hello"):
#     print(greeting, name!)

# Call the function with and without arguments
# greet()  # Uses default values
# greet("Nikolozi")  # Uses default greeting
# greet("Luka", "Hi")  # Uses custom values

# 62) Create a script that uses a function with keyword arguments.

# Define a function with keyword arguments
# def describe_person(name, age, city="Unknown"):
    # print(f"{name} is {age} years old and lives in {city}.")

# Call the function with keyword arguments
# describe_person(name = "Nikolozi", age = 15, city = "Tbilisi")
# describe_person(name = "Luka", age = 22)  # Uses default value for city

# 63) Write a program that uses all basic arithmetic operators (+, -, *, /, %, //, **) with two numbers.
# Define two numbers
# a = 10
# b = 3

# Perform arithmetic operations
# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# modulus = a % b
# floor_division = a // b
# exponentiation = a ** b

# Print results
# print(f"Addition: {a} + {b} = {addition}")
# print(f"Subtraction: {a} - {b} = {subtraction}")
# print(f"Multiplication: {a} * {b} = {multiplication}")
# print(f"Division: {a} / {b} = {division}")
# print(f"Modulus: {a} % {b} = {modulus}")
# print(f"Floor Division: {a} // {b} = {floor_division}")
# print(f"Exponentiation: {a} ** {b} = {exponentiation}")

# 64) Create a script to demonstrate the use of assignment operators (=, +=, -=, *=, /=, %=, //=, **=).

# Initialize a variable
# number = 10

# Use assignment operators
# number += 5  # Equivalent to number = number + 5
# print(f"After +=: {number}")

# number -= 3  # Equivalent to number = number - 3
# print(f"After -=: {number}")

# number *= 2  # Equivalent to number = number * 2
# print(f"After *=: {number}")

# number /= 4  # Equivalent to number = number / 4
# print(f"After /=: {number}")

# number %= 3  # Equivalent to number = number % 3
# print(f"After %=: {number}")

# number //= 2  # Equivalent to number = number // 2
# print(f"After //=: {number}")

# number **= 3  # Equivalent to number = number ** 3
# print(f"After **=: {number}")

# 65) Write a program to compare two numbers using comparison operators (==, !=, >, <, >=, <=).

# Define two numbers
# a = 10
# b = 5

# Compare the numbers
# print(f"{a} == {b}: {a == b}")
# print(f"{a} != {b}: {a != b}")
# print(f"{a} > {b}: {a > b}")
# print(f"{a} < {b}: {a < b}")
# print(f"{a} >= {b}: {a >= b}")
# print(f"{a} <= {b}: {a <= b}")

# 66) Demonstrate the use of logical operators (and, or, not) in a simple condition.

# Define boolean variables
# x = True
# y = False

# Use logical operators
# print(f"x and y: {x and y}")
# print(f"x or y: {x or y}")
# print(f"not x: {not x}")
# print(f"not y: {not y}")

# Example with conditions
# a = 10
# b = 20
# print(f"(a > 5) and (b < 25): {(a > 5) and (b < 25)}")
# print(f"(a > 15) or (b < 25): {(a > 15) or (b < 25)}")
# print(f"not (a < 15): {not (a < 15)}")

# 67) Create a script that shows the use of bitwise operators (&, |, ^, ~, <<, >>).
# Define two numbers
# a = 12  # Binary: 1100
# b = 5   # Binary: 0101

# Perform bitwise operations
# and_op = a & b      # Bitwise AND
# or_op = a | b       # Bitwise OR
# xor_op = a ^ b      # Bitwise XOR
# not_op = ~a         # Bitwise NOT
# left_shift = a << 2 # Left shift
# right_shift = a >> 2 # Right shift

# Print results
# print(f"{a} & {b} = {and_op}")
# print(f"{a} | {b} = {or_op}")
# print(f"{a} ^ {b} = {xor_op}")
# print(f"~{a} = {not_op}")
# print(f"{a} << 2 = {left_shift}")
# print(f"{a} >> 2 = {right_shift}")

# 68) Write a program that checks if a number is within a specified range using comparison and logical operators.
# Define a number and a range
# number = 15
# lower_bound = 10
# upper_bound = 20

# Check if the number is within the range
# if lower_bound <= number <= upper_bound:
#     print(f"{number} is between {lower_bound} and {upper_bound}.")
# else:
#     print(f"{number} is not between {lower_bound} and {upper_bound}.")

# 69) Use identity operators (is, is not) to compare objects and variables.

# Define some variables
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# Identity comparisons
# print(f"a is b: {a is b}")       # True, because b is a reference to a
# print(f"a is c: {a is c}")       # False, because c is a different list object
# print(f"a is not c: {a is not c}") # True, because a and c are different objects

# 70) Demonstrate the use of operator precedence by creating a complex expression.
# Define a list
# fruits = ["apple", "banana", "cherry"]

# Check membership
# print(f"apple in fruits: {'apple' in fruits}")
# print(f"grape in fruits: {'grape' not in fruits}")

#  71) Demonstrate the use of operator precedence by creating a complex expression.
# Demonstrate operator precedence
# a = 10
# b = 5
# c = 2

# Complex expression
# result = a + b * c / (c - 1) ** 2
# print(result)

# 72) Write a program that takes two user inputs and performs all the basic arithmetic operations on them.
# Take user inputs
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")
# print(f"{num1} % {num2} = {num1 % num2}")
# print(f"{num1} // {num2} = {num1 // num2}")
# print(f"{num1} ** {num2} = {num1 ** num2}")

# 73) Create a script that swaps the values of two variables without using a third variable.
# Define two variables
# a = 5
# b = 10

# Swap values using tuple unpacking
# a, b = b, a

# Print the swapped values
# print(f"After swapping: a = {a}, b = {b}")

# 74) Create a list of five numbers and print the list.

# list = [1,2,3,4,5]
# print(list)

# 75) Write a program to access elements from a list using positive and negative indexing.

# Define a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Access elements using positive indexing
# print(fruits[0])
# print(fruits[1])
# print(fruits[4])

# Access elements using negative indexing
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-5])

# 76) Create a script to add, remove, and update elements in a list.
# Create a script to add, remove, and update elements in a list.

# Define a list
# fruits = ["apple", "banana", "cherry"]

# Add elements to the list
# fruits.append("date")  # Add to the end
# print("After appending 'date':", fruits)

# fruits.insert(1, "blueberry")  # Add at specific index
# print("After inserting 'blueberry' at index 1:", fruits)

# Remove elements from the list
# fruits.remove("banana")  # Remove by value
# print("After removing 'banana':", fruits)

# popped_fruit = fruits.pop(2)  # Remove by index
# print(f"After popping element at index 2 ({popped_fruit}):", fruits)

# Update elements in the list
# fruits[1] = "blackberry"  # Update element at index 1
# print(fruits)

# 77) Write a program that concatenates two lists.

# Define two lists
# list1 = ["apple", "banana", "cherry"]
# list2 = ["date", "elderberry", "fig"]

# Concatenate the lists
# concatenated_list = list1 + list2
# print("Concatenated list:", concatenated_list)

# 78) Create a script that finds the length of a list using the len() function.

# Define a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Find the length of the list
# length = len(fruits)
# print("Length of the list:", length)

# 79) Write a program that checks if a specified element is present in a list.

# Define a list
# fruits = ["apple", "banana", "cherry"]

# Check if an element is present in the list
# element = "banana"
# if element in fruits:
#     print(f"{element} is present in the list.")
# else:
#     print(f"{element} is not present in the list.")

# 80) Create a script to slice a list and print the sliced list.

# Define a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Slice the list
# sliced_list = fruits[1:4]  # Slicing from index 1 to 3 (end index is not included)
# print(sliced_list)

# Another slicing example
# sliced_list = fruits[:3]  # Slicing from the beginning to index 2
# print(sliced_list)

# sliced_list = fruits[2:]  # Slicing from index 2 to the end
# print(sliced_list)

# 81) Write a program that sorts a list in ascending and descending order.
# Define a list of numbers
# numbers = [4, 2, 9, 1, 5, 6]

# Sort the list in ascending order
# numbers.sort()
# print("List sorted in ascending order:", numbers)

# Sort the list in descending order
# numbers.sort(reverse=True)
# print("List sorted in descending order:", numbers)

# 82) Create a script that demonstrates the use of list comprehension.
# Define a list of numbers
# numbers = [1, 2, 3, 4, 5]

# Use list comprehension to create a list of squares
# squares = [x**2 for x in numbers]
# print("List of squares:", squares)

# Use list comprehension with a condition
# even_squares = [x**2 for x in numbers if x % 2 == 0]
# print("List of squares of even numbers:", even_squares)

# Create a list of strings and use list comprehension to convert to uppercase
# words = ["hello", "world", "python"]
# uppercase_words = [word.upper() for word in words]
# print("List of uppercase words:", uppercase_words)

# 83) Write a program to find the maximum and minimum values in a list.
# Define a list of numbers
# numbers = [4, 2, 9, 1, 5, 6]

# Find the maximum and minimum values
# max_value = max(numbers)
# min_value = min(numbers)
# print(max_value)
# print(min_value)

# 84) Create a script that reverses the elements of a list.
# Define a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Reverse the list
# fruits.reverse()
# print(fruits)

# Another way to reverse the list using slicing
# reversed_fruits = fruits[::-1]
# print(reversed_fruits)

# 85) Write a program that prints numbers from 1 to 10 using a while loop.

# Initialize counter
# num = 1

# Use a while loop to print numbers from 1 to 10
# while num <= 10:
#     print(num)
#     num += 1

# 86) Create a script that calculates the sum of the first 10 natural numbers using a while loop.

# Initialize variables
# num = 1
# sum = 0

# Use a while loop to calculate the sum of the first 10 natural numbers
# while num <= 10:
#     sum += num
#     num += 1

# print(sum)

# 87) Write a program that prints the multiplication table of a given number using a while loop.

# Given number
# number = 5
# Initialize counter
# i = 1

# Use a while loop to print the multiplication table
# while i <= 10:
#     print(f"{number} x {i} = {number * i}")
#     i += 1

# 88) Create a script that finds the factorial of a number using a while loop.

# Given number
# number = 5
# Initialize variables
# factorial = 1
# i = 1

# Use a while loop to calculate the factorial
# while i <= number:
#     factorial *= i
#     i += 1

# print(f"The factorial of {number} is {factorial}")

# 89) Write a program that prints all even numbers between 1 and 50 using a while loop.

# Initialize counter
# num = 1

# Use a while loop to print all even numbers between 1 and 50
# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# 90) Create a script that reverses a given number using a while loop.

# Given number
# number = 12345
# Initialize variables
# reversed_number = 0

# Use a while loop to reverse the number
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number //= 10

# print(reversed_number)

# 91) Write a program that calculates the sum of digits of a number using a while loop.

# Given number
# number = 12345
# Initialize variable
# sum_of_digits = 0

# Use a while loop to calculate the sum of digits
# while number > 0:
#     digit = number % 10
#     sum_of_digits += digit
#     number //= 10

# print(sum_of_digits)

# 92) Create a script that finds the greatest common divisor (GCD) of two numbers using a while loop.

# Given numbers
# a = 48
# b = 18

# Use a while loop to find the GCD using the Euclidean algorithm
# Define two numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# Use a while loop to find the GCD
# while b != 0:
#     a, b = b, a % b

# print(a)


# print(a)

# 93) Write a program that prints the Fibonacci sequence up to a specified number using a while loop.

# Specified limit
# limit = 50

# Initialize variables
# a, b = 0, 1

#  Use a while loop to print the Fibonacci sequence
# while a <= limit:
#     print(a, end=" ")
#     a, b = b, a + b
# print()  # For a new line at the end

# 94) Create a script that prints numbers from 1 to 100, but skips numbers divisible by 5, using a while loop.
# Initialize a counter
# num = 1

# Use a while loop to print numbers from 1 to 100, skipping those divisible by 5
# while num <= 100:
#     if num % 5 != 0:
#         print(num)
#     num += 1  # Increment the counter

# 95) Write a program that prints each element of a list using a for loop.

# Define a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Use a for loop to print each element
# for fruit in fruits:
#     print(fruit)

# 96) Create a script that prints numbers from 1 to 10 using a for loop.

# Use a for loop to print numbers from 1 to 10
# for num in range(1, 11):
#     print(num)

# 97) Write a program that calculates the sum of elements in a list using a for loop.

# Define a list of numbers
# numbers = [1, 2, 3, 4, 5]

# Initialize the sum
# total_sum = 0

# Use a for loop to calculate the sum of elements
# for num in numbers:
#     total_sum += num

# print(total_sum)

# 98) Create a script that prints the multiplication table of a given number using a for loop.

# Define the number
# number = int(input("Enter a number for the multiplication table: "))

# Use a for loop to print the multiplication table
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# 99) Write a program that prints all even numbers between 1 and 50 using a for loop.

# Use a for loop to print even numbers between 1 and 50
# for num in range(1, 51):
#     if num % 2 == 0:
#         print(num)

# 100) Write a program that iterates over a dictionary and prints each key-value pair.

# Define the upper limit
# limit = int(input("Enter the upper limit for Fibonacci sequence: "))

# Initialize variables
# a, b = 0, 1

# Use a for loop to print the Fibonacci sequence
# print(a)
# print(b)
# for _ in range(limit - 2):
#     a, b = b, a + b
#     print(b)

# 101)  Write a program that iterates over a dictionary and prints each key-value pair.

# Define a dictionary
# person = {"name": "Nikolozi", "age": 15, "city": "Tbilisi"}

# Use a for loop to iterate over the dictionary
# for key, value in person.items():
#     print(f"{key}: {value}")

# 102) Create a script that finds the maximum and minimum values in a list using a for loop.

# Define a list of numbers
# numbers = [4, 2, 9, 1, 5, 6]

# Initialize max and min variables
# max_value = numbers[0]
# min_value = numbers[0]

# Use a for loop to find the maximum and minimum values

# for num in numbers:
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num

# print(f"The maximum value is {max_value}")
# print(f"The minimum value is {min_value}")

# 103) Create a script that prints the reverse of a list using a for loop.

# Define a string
# text = "Hello, World!"

#     print(char)