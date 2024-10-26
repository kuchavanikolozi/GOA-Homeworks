# 1) This code does not execute properly. Try to figure out why.
# def multiply(a, b):
#     a * b

def multiply(a, b):
   return a * b

# 2) We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)

# 3) We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number(s):
    return int(s)

# 4) In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

def make_negative(number):
    if number > 0:
        return -number
    else:
        return number