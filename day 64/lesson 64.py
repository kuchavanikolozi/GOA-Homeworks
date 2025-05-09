# codewars


# 1) 

# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.

def is_opposite(s1,s2):
    return bool(s1) and s1.swapcase() == s2 

# 2)

# While making a game, your partner, Greg, decided to create a function to check if the user is still alive called checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.

def check_alive(health):
    return health > 0

# 3)

# Define a method named countCharOccurrences or count_char_occurrences that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int.

def count_char_occurrences(strng, char):
    return strng.count(char)

# 4) 

# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

def remove(st):
    cleaned = st.replace('!', '')
    return cleaned + '!'