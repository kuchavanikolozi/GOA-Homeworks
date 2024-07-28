# We need to create a program where our name will be printed 10 times using a for loop

for i in range(11):
    print("Nikolozi")

# We need to create a program that will print only even numbers from 0 to 10 using a for loop.

for number in range(11):  
    if number % 2 == 0:  
        print(number)  

# We need to create a program that will add even numbers from 0 to 10 and finally print the sum of even numbers outside the For loop: hint:
# Above the for loop, let's create one variable named result, which will be added to the numbers that turned out to be even as a result of the comparison.

result = 0

for number in range(11):  
    if number % 2 == 0:  
        result += number  

print(result)