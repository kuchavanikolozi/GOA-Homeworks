# codewars

# 1) You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    total = 0  
    
    for x in arr:  
        if x > 0:  
            total += x 
    
    return total

# 2) Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    return sum(x**2 for x in numbers)

# 3) Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2