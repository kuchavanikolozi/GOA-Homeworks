# Codewars

# 1) 
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse=True)))

# 2) 
# Complete the solution so that it returns true if the first argument(string) 
# passed in ends with the 2nd argument (also a string).

# def solution(text, ending):
    # return text.endswith(ending)

# 3) 
# In this kata you will create a function that takes a list of non-negative 
# integers and strings and returns a new list with the strings filtered out.

# def filter_list(l):
#     return [x for x in l if isinstance(x, int)]

# 4) 
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" 
# for the development and functioning of living organisms.
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# Your function receives one side of the DNA (string, except for Haskell); you need to return 
# the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# def DNA_strand(dna):
#     complement = {
#         'A': 'T',
#         'T': 'A',
#         'C': 'G',
#         'G': 'C'
#     }

#     return ''.join(complement[nucleotide] for nucleotide in dna)

# 5) 
# Complete the function that accepts a string parameter, 
# and reverses each word in the string. 
# All spaces in the string should be retained.

# def reverse_words(text):
#     words = text.split(' ') 
#     reverse_words = [word[::-1] for word in words]
#     return ' '.join(reverse_words)

# 6)

# The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.
# However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. 
# \Do not mutate the original array/list. '
# If there are multiple elements with the same value, remove the one with the lowest index. 
# If you get an empty array/list, return an empty array/list.

# def remove_smallest(numbers):
#     if not numbers:
#         return []

#     min_value = min(numbers)
    
#     min_index = numbers.index(min_value)
    
#     return numbers[:min_index] + numbers[min_index + 1:]

# 7)

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# def disemvowel(string_):
#     vowels = "aeiouAEIOU"
#     return ''.join(char for char in string_ if char not in vowels)

# 8)
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)

# def stray(arr):
#     result = 0
#     for number in arr:
#         result ^= number
#     return result