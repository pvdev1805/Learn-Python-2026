# Day 1: Hello, Python!
# 1. print() function
print("Hello, Python!")
print("This is my first Python script in 2026")

# 2. Comments
# This is a single-line comment
"""
This is a multi-line comment
that can span multiple lines.
"""

# 3. Variables
greeting = "Hello, Python!"
print(greeting)

# 4. Data Types
# String
name = "Alice"
# Integer
age = 30
# Float
height = 5.5
# Boolean
is_student = True
print(name, age, height, is_student)

# 5. Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus: 1
print(a // b)  # Floor division: 3
print(a ** b)  # Exponentiation: 1000

# 6. Comparison Operators
x = 10
y = 20
print(x == y)  # False
print(x != y)  # True
print(x > y)  # False
print(x < y)  # True
print(x >= y)  # False
print(x <= y)  # True

# 7. Logical Operators
print(x > 5 and y < 30)  # True
print(x > 15 or y < 30)  # True
print(not (x > 5))  # False

# 8. Assignment Operators
z = 10
z += 5  # 15
z -= 3  # 12
z *= 2  # 24
z /= 4  # 6.0
z %= 5  # 1.0
z //= 2  # 0.0
z **= 3  # 0.0
print(z)

# 9. Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)  # True
print(list1 is list3)  # False
print(list1 is not list3)  # True

# 10. Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False
print(6 not in my_list)  # True

# 11. Bitwise Operators
x = 5  # 0101
y = 3  # 0011
print(x & y)  # 1
print(x | y)  # 7
print(x ^ y)  # 6
print(~x)  # -6
print(x << 1)  # 10
print(x >> 1)  # 2

# 12. Operator Precedence
result1 = 3 + 4 * 2  # 11
result2 = (3 + 4) * 2  # 14
print(result1)
print(result2)

# 13. Type Conversion
s = "10"
num1 = int(s)  # 10
num2 = float(s)  # 10.0
print(num1)
print(num2)
