# Codewars

# 1)

# Create a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".

def greet(name):
    return f"Hello, {name} how are you doing today?"

# 2)

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

def litres(time):
    return int(time * 0.5)


# 3)

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return true if you're better, else false!

def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average

# 4)

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    return [-x for x in lst]

# 5)

# 