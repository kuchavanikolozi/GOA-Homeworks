# print() ფუნქცია გამოდის კონსოლში რაიმე ტექსტს, რიცხვს ან ცვლადის მნიშვნელობას.

print("Hello World!")  # ტერმინალში გამოდის: Hello World!

# int() ფუნქცია კონვერტაციას ახდენს რიცხვს მთელი რიცხვად.
number = int("123")  # ტერმინალში გამოდის: 123

# float() ფუნქცია რიცხვის კონვერტაციას ახდენს ათწილადებად.
float = float("1234")  # ტერმინალში გამოდის: 1234.0
print(float)

# str() ფუნქცია კონვერტაციას ახდენს ობიექტს სტრიქონად.
string = str(123)  # ტერმინალში გამოდის: "123"

# input() ფუნქცია მომხმარებელს სთხოვს შეიყვანოს მონაცემები და აბრუნებს მას სტრიქონად.

name = input("Please input your name: ")  # მომხმარებლის შეყვანის შემდეგ აბრუნებს სტრიქონს

# range() ფუნქცია ქმნის რიცხვების მიმდევრობას.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4