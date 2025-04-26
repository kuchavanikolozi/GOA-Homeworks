# Codewars

# 1)

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return true if you're better, else false!



def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average

# 2)

# The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.
# However, there is a bug in the method that needs to be resolved.

def kata_13_december(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.pop(i)
        else:
            i += 1
    return lst

# 3)

def get_drink_by_profession(param):
        drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
        return drinks.get(param.lower(), "Beer")


# 4) 

# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    return sum(x**2 for x in numbers)

# 5)

# For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"