# 1) მომხმარებელს შემოვატანინოთ რიცხვი, და გავარკვიოთ ლუწია თუ კენტი.

# def even_or_odd():
#     number = int(input("Please input an number: "))
#     if number % 2 == 0:
#         print("Number is odd.")
#     else:
#         print("Number is even.")

# 2) მომხმარებელს შემოვატანინოთ რიცხვი, და გავარკვიოთ, დადებითია თუ უარყოფითი.

# def positive_or_negative():
#     number = int(input("Please input an number: "))
#     if number > 0:
#         print("Number is Positive.")
#     elif number < 0:
#         print("Number is Negative.")
#     else:
#         print("Number is equal to 0.")

# 3) მომხმარებელს შემოვატანინოთ რიცხვი, და დავუბეჭდოთ არის თუ არა ეს რიცხვი 5-ის ჯერადი.

# def multiple_of_five():
#     number = int(input("Please input an number: "))
#     if number % 5 == 0:
#         print("Number is multiply of 5.")
#     else:
#         print("Number is not multiply of 5.")

# 4) მომხმარებელს შემოვატანინოთ მისი ასაკი, და თუ თვრამეტი წლის არის ან მეტი დავუბეჭდოთ რომ ის ზრდასრულია, სხვა შემთხვევაში დავუბეჭდოთ
# რომ ის არარის ზრდასრული.

# def check_adulthood():
#     age = int(input("Please input your age: "))
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are not adult.")

# 5) მომხმარებელს შემოვატანინოთ რიცხვი, ავიყვანოთ ეს რიცხვი კვადრატში.

# def square_number():
#     number = int(input("Please input an number: "))
#     print(number ** 2)

# 6) მომხმარებელს უნდა შემოვატანინოთ პაროლი, შემდეგ კი გავიგოთ პაროლის სიგრძე.

# def check_password():
#     while True:
#         password = input(": ")
#         if len(password) >= 8:
#             print("რეგისტრაცია წარმატებით დასრულდა!")
#             break
#         else:
#             print("პაროლი უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს.")

# 7) მომხმარებელს შემოვატანინოთ რიცხვი, და ამ რიცხვის კვადრატი დავუბეჭდოთ 10-ჯერ.

# def squares_of_numbers():
#     numbers = []
#     for _ in range(10):
#         number = int(input("Please input an number: "))
#         numbers.append(number)
#     for number in numbers:
#         print(number ** 2)