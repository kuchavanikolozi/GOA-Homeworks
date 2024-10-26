# We need to create a list and print the first, second and 
# third element from the bottom - using indexes, and describe what is actually happening behind it.

cars = ["Toyota", "BMW", "Mercedes", "Honda", "Ford"]

print("ბოლოდან პირველი ელემენტი:", cars[-1])
print("ბოლოდან მეორე ელემენტი:", cars[-2])
print("ბოლოდან მესამე ელემენტი:", cars[-3])

# მეორე დავალება

# We need to use slicing to slice the first 3 elements of the list

cars = ["Toyota", "BMW", "Mercedes", "Honda", "Ford"]

first_three_cars = cars[:3]

print(first_three_cars)

# მესამე დავალება

# We should use slicing to print the elements at the index every 3 times
cars = ["Toyota", "BMW", "Mercedes", "Honda", "Ford", "Chevrolet", "Nissan", "Kia", "Hyundai"]

every_third_car = cars[::3]

print("ყოველი მესამე ელემენტი სიაში:", every_third_car)