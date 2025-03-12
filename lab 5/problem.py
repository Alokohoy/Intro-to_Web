name = "Burkhan"
print("Name:", name)

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

x, y = 5, 10
x, y = y, x
print("After swapping: x =", x, ", y =", y)

PI = 3.14159
radius = 5
area = PI * (radius ** 2)
print("Area of circle:", area)

# problem 2 #
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hi {name}, you are {age} years old!")

# 2. Sum, Average, and Product
num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())

total = num1 + num2 + num3
average = total / 3
product = num1 * num2 * num3

print(f"Sum: {total}, Average: {average}, Product: {product}")



