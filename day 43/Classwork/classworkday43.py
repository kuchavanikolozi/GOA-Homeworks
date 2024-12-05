# codewars

# 1) 
# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return repeat * string

# 2)
# Given an array of integers your solution should find the smallest integer.
# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# 3)
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    return sum(x**2 for x in numbers)