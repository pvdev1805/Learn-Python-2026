# Day 2: Input and Output

# 1. input() function
name = input("Enter your name: ")  # Prompts the user to enter their name
age = input("Enter your age: ")  # Prompts the user to enter their age
print("Hello, " + name + "! You are " + age + " years old.")

# Type conversion with input()
age = int(input("Enter your age: "))  # Converts the input to an integer
height = float(input("Enter your height in meters: "))  # Converts the input to a float
print("You are " + str(age) + " years old and " + str(height) + " meters tall.")

# 2. Output Formatting
name = "Alice"
age = 30
height = 1.75
print(f"Hello, {name}! You are {age} years old and {height} meters tall.")

# 3. If-Else Statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# If-elif-else statement
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Nested If Statements
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# 5. match-case Statements (Python 3.10+)
command = input("Enter a command: ")
match command:
    case "start":
        print("Starting the program...")
    case "stop":
        print("Stopping the program...")
    case _:
        print("Unknown command.")

# 6. for Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

# 7. while Loops
count = 0
while count < 5:
    print(count)
    count += 1

# 8. break and continue Statements
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# 9. pass Statement
def my_function():
    pass


class MyClass:
    pass


# 10. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# 11. Ternary Operator
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(f"You are an {status}.")

# 12. List Comprehensions
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)
