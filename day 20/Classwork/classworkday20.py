# პირველი დავალება

# def - ით ვიმარტივებ საქმეს, და არ ვწვალობ, ასევე არ ვარღვევ DRY - ს წესს
# for i in range ით კი ვბეჭდავ იმდენჯერ, სადამდეც საჭიროა

# def print_numbers():
#     for i in range(1, 21):
#         print(i)

# ფუნქციის გამოძახება
# print_numbers()

# მეორე დავალება

# ამ ფუნქციაში, 
# ჩვენ ვიყენებთ for ციკლს 1-დან 20-ის ჩათვლით რიცხვების გასავლელად და total ცვლადში ვამატებთ თითოეულ რიცხვს.
#  საბოლოოდ, ციკლის დასრულების შემდეგ, print ფუნქციით ვბეჭდავთ ჯამს

# def sum_numbers():
#     total = 0
#     for i in range(1, 21):
#         total += i
#     print(total)

# ფუნქციის გამოძახება
# sum_numbers()

# მესამე დავალება

# def print_range(start, end):
#     for i in range(start, end + 1):
#         print(i)

# ფუნქციის გამოძახება მაგალითისთვის
# print_range(5, 10)

# მეოთხე დავალება

# def sum_user_numbers():
#     # მომხმარებლისგან რიცხვების შეყვანა
#     num1 = float(input("გთხოვთ შემოიტანეთ პირველი რიცხვი: "))
#     num2 = float(input("გთხოვთ შემოიტანეთ მეორე რიცხვი: "))
    
#     # რიცხვების ჯამის გამოთვლა
#     total = num1 + num2
    
#     # ჯამის დაბეჭდვა
#     print("ორივე რიცხვის ჯამი არის:", total)

#  ფუნქციის გამოძახება
# sum_user_numbers()

# მეხუთე დავალება

# def multiply_range():
#     # მომხმარებლისგან რიცხვების შეყვანა
#     start = int(input("გთხოვთ შემოიტანეთ პირველი რიცხვი: "))
#     end = int(input("გთხოვთ შემოიტანეთ მეორე რიცხვი: "))

#     # ნამრავლის გამოთვლა
#     product = 1

#     # რიცხვების ნამრავლის გამოთვლა
#     for i in range(start, end + 1):
#         product *= i
 
# ფუნქციის გამოძახება
# multiply_range()

# მეექვსე დავალება

# def list(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# numbers = [1, 2, 3, 4, 5]
# result = list(numbers)
# print("სიის ჯამი არის:", result)

# მეშვიდე დავალება

# def list(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total


# numbers = [1, 2, 3, 4, 5]
# result = list(numbers)
# print("result")