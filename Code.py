# Here is the code of our Calculator- 
first = input("Enter your first number : ")
second = input("Enter your second number : ")
first = int(first)
second = int(second)
print("----Enter required keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")
print("Thank You!")
