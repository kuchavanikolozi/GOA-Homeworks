# პირველი დავალება

# We need to create a function that will print numbers from 1 to 20 inclusive.

def print_numbers():
    for number in range(1, 21):
        print(number)

print_numbers()

# მეორე დავალება
# We need to create a function that will print the sum of numbers from 1 to 20 inclusive.

def print_sum_of_numbers():
    total_sum = sum(range(1, 21))
    print(total_sum)

print_sum_of_numbers()

# მესამე დავალება

# We need to create a function that will pass two numbers, 
# start, end, and then add all the numbers from start to end between these numbers.
def print_numbers_between(start, end):
    for number in range(start, end + 1):
        print(number)

print_numbers_between(5, 10)

# მეოთხე დავალება

# We need to create a function that will pass one number (end), and then from 0 to 
# that number and calculate the sum of all the numbers.
# Finally, return that value from the function and print it.

def calculate_sum(end):
    total = 0
    for number in range(end + 1):
        total += number
    return total