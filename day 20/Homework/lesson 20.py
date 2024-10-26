# we need to create an example of for cycles with lists combination

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# numbers1 = [1, 2, 3, 4, 5]
# for num in numbers1:
#     print(num * num)

# numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers2:
#     if num % 2 == 0:
#         print(num)

# words = ["hello", "world", "python"]
# for word in words:
#     print(word[0])

# numbers3 = [1, 2, 3, 4, 5]
# for num in numbers3:
#     print(num * 2)

# numbers4 = [1, 6, 3, 8, 5, 10]
# for num in numbers4:
#     if num > 5:
#         print(num)

# numbers5 = [5, 10, 15, 20, 25]
# for num in numbers5:
#     print(num - 1)

# numbers6 = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(total)

# We need to come up with some functions and explain what specific functions do (at least 5)

# 1)
# def add_numbers(a, b):
#     return a + b
# ეს ფუნქცია იღებს ორ რიცხვს (a და b) შესაყვანად და აბრუნებს მათ ჯამს, გამოვიძახებთ add_numbers(3, 4), ის დაგვიბრუნებს 7-ს.

# 2)
# def max_of_three(a, b, c):
#     return max(a, b, c)
# ეს ფუნქცია შეყვანის სახით იღებს სამ რიცხვს და აბრუნებს სამიდან ყველაზე დიდს ჩაშენებული max ფუნქციის გამოყენებით, თუ გამოვიძახებთ max_of_three(3, 7, 5), ის დაგვიბრუნებს 7-ს.

# 3)
# def is_even(number):
#     return number % 2 == 0
# ეს ფუნქცია შესაყვანად იღებს რიცხვს და აბრუნებს True-ს, თუ რიცხვი ლუწია (ნაშთის გარეშე იყოფა 2-ზე), ხოლო წინააღმდეგ შემთხვევაში - False. თუ გამოვიძახებთ is_even(4), ის დააბრუნებს True-ს.

# 4)
# def rectangle_area(length, width):
#     return length * width
# ეს ფუნქცია იღებს მართკუთხედის სიგრძესა და სიგანეს შეყვანის სახით და აბრუნებს მის ფართობს (სიგრძე გამრავლებული სიგანეზე). მაგალითად, rectangle_area(5, 3) აბრუნებს 15-ს.

# 5)
# def average(a, b):
#     return (a + b) / 2
# ეს ფუნქცია ითვლის ორ a და b რიცხვის საშუალოს. ის აერთიანებს მათ და ყოფს 2-ზე საშუალო მნიშვნელობის მისაღებად.

# For Loop:
#We need to Print all integers from 0 to 20 inclusive.

# for i in range(21):
#     print(i)

# We need to Print the first 10 natural numbers.

# for i in range(1, 11):
#     print(i)

# We need to Print even numbers separately and odd numbers separately from 0 to 100 inclusive.

# Print even numbers

# print("Even numbers: ")
# for i in range(0, 101, 2):
#     print(i)

# Print odd numbers

# print("Odd numbers: ")
# for i in range(1, 101, 2):
#     print(i)

# We need to Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

# num = int(input("Please input a number: "))
# total_sum = 0
# for i in range(1, num + 1):
#     total_sum = total_sum + i
# print("The sum of all numbers from 1 to", num, "is:", total_sum)

# We need to Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive

# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)

# While Loop

# We need to Print even numbers up to 20.
# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# We need to calculate the sum of numbers from 1 to 10.

# num = 1
# sum_numbers = 0
# while num <= 10:
#     sum_numbers += num
#     num += 1
# print("The sum of numbers from 1 to 10 is:", sum_numbers)

# correct_number = 7
# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess == correct_number:
#         print("Congratulations! You guessed the correct number.")
#         break  # Exit the loop if the guess is correct
#       else:
#         print("Wrong guess. Try again.")

# Write a while loop that processes a list of numbers, doubling each number, and prints the new list.
 
# numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(numbers):
#     # Double each number in the list
#     numbers[index] *= 2
#     index += 1
# print("Doubled numbers:", numbers)

# We need to Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

# correct_password = "password123"
# password_entered = False

# while password_entered == False:
#     password = input("Please enter the password: ")
#     if password == correct_password:
#         print("Correct password entered. Access granted.")
#         password_entered = True  
#     else:
#         print("Incorrect password. Please Try again.") 