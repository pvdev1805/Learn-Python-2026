# Day 3: Functions

# 1. Function Definition
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # Output: Hello, Alice!


# 2. Function Parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")  # Output: Hello, Alice!
greet("Bob", greeting="Hi")  # Output: Hi, Bob!


def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3))  # Output: 6


# 3. Return Statement
def add(a, b):
    return a + b


result = add(5, 3)
print(result)  # Output: 8

# 4. Lambda Functions
add_lambda = lambda a, b: a + b
result_lambda = add_lambda(5, 3)
print(result_lambda)  # Output: 8


# 5. Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120


# 6. Docstrings
def greet_with_doc(name):
    """This function takes a name as input and prints a greeting message.
    Parameters:
    name (str): The name of the person to greet.
    Returns:
    None
    """
    print(f"Hello, {name}!")


# 7. Function Annotations
def greet_annotated(name: str) -> None:
    """This function takes a name as input and prints a greeting message.
    Parameters:
    name (str): The name of the person to greet.
    Returns:
    None
    """
    print(f"Hello, {name}!")


# 8. Global and Local Variables
x = 10  # Global variable


def modify_global():
    global x  # Declare that we want to modify the global variable x
    x += 5  # Modify the global variable


modify_global()
print(x)  # Output: 15


# 9. Variable Scope
def outer_function():
    x = 10  # Local variable in outer_function

    def inner_function():
        print(x)  # Accessing variable from enclosing scope

    inner_function()


outer_function()  # Output: 10


# 10. Higher-Order Functions
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)  # Using map to apply the square function to each element in the numbers list
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
