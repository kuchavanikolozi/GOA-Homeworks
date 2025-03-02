# Python Lists

# 1) Write a script to create and print a list.

my_list = ["apple", "banana", "cherry"]
print(my_list)

# 2) Create a script to add and remove elements from a list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)


# 3) Write a script to sort a list.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

# 4) Demonstrate the use of list comprehension

squares = [x**2 for x in range(1, 6)]
print(squares)


# 5) Create a script to find the length of a list.

animals = ["cat", "dog", "elephant", "tiger"]
print(len(animals))

# Python If...Else

# 1) Write a script that uses an if statement to check a condition.

age = 18
if age >= 18:
    print("You are eligible to vote.")


# 2) Create a script that uses an if-else statement.

number = 10
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3) Write a script that uses an if-elif-else statement.

grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Fail")

# 4) Demonstrate nested if statements.

x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")

# 5) Write a script that uses the ternary operator.

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Python While Loops

# 1) Write a script to demonstrate a while loop.

count = 1
while count <= 5:
    print(count)
    count += 1

# 2) Create a script that uses a while loop with a break statement.

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# 3) Write a script that uses a while loop with a continue statement.

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

# 4) Demonstrate an infinite loop and how to stop it.

while True:
    response = input("Type 'stop' to end: ")
    if response.lower() == 'stop':
        break

# 5) Create a script that uses a while loop to iterate over a list.

colors = ["red", "green", "blue"]
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

# Python For Loops

# 1) Write a script to demonstrate a for loop.

for i in range(1, 6):
    print(i)

# 2) Create a script that uses a for loop to iterate over a list.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3) Write a script that uses a for loop with the range() function.

for x in range(5):
    print(x)

# 4) Demonstrate nested for loops.

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 5) Create a script that uses a for loop with an else clause.

for x in range(3):
    print(x)
else:
    print("Loop completed")
