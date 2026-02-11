# Python Basics

## Day 1 - Hello World

### 1. print()

This function is used to display output on the console. It can take multiple arguments and will print them as a single
line of text.

Syntax: **print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)**

- **value1, value2, ...** : These are the values that you want to print. They can be of any data type (string, integer,
  float, etc.).
- **sep** : This is an optional parameter that specifies the separator between the values. By default, it is a
  space (' ').
- **end** : This is an optional parameter that specifies what to print at the end of the output. By default, it is a
  newline
  character ('\n'), which means that the next print statement will start on a new line.
- **file** : This is an optional parameter that specifies the file to which the output should be written. By default, it
  is
  sys.stdout, which means that the output will be printed to the console.
- **flush** : This is an optional parameter that specifies whether to flush the output buffer after printing. By
  default, it
  is False, which means that the output will be buffered and may not appear immediately on the console.

Example usage:

```python
print("Hello, World!")  # Output: Hello, World!
```

### 2. Comments

Comments are used to explain the code and make it more readable. They are ignored by the Python interpreter and do not
affect the execution of the program.
In Python, there are two types of comments:

- Single-line comments: These are created using the hash symbol (#). Anything following the hash symbol on the same line
  is considered a comment.
- Multi-line comments: These are created using triple quotes (''' or """). Anything between the triple quotes is
  considered a comment, even if it spans multiple lines.

Example usage:

```python
# This is a single-line comment 
'''
This is a multi-line comment
that spans multiple lines
'''
```

### 3. Variables

Variables are used to store data in a program. In Python, you can create a variable by simply assigning a value to it.
The variable name can be any valid identifier, and it can hold any data type (string, integer, float, etc.).
Syntax: **variable_name = value**
Example usage:

```python
name = "Alice"  # This is a string variable
age = 30  # This is an integer variable
height = 5.5  # This is a float variable
```

### 4. Data Types

Python has several built-in data types that are used to store different kinds of data. Some of the most common data
types in Python include:

- **int**: Used to store integer values (e.g., 1, 2, 3).
- **float**: Used to store floating-point numbers (e.g., 3.14, 2.718).
- **str**: Used to store strings (e.g., "Hello", "World").
- **bool**: Used to store boolean values (True or False).
- **list**: Used to store a collection of items (e.g., [1, 2, 3]).
- **tuple**: Used to store an ordered collection of items that cannot be modified (e.g., (1, 2, 3)).
- **dict**: Used to store key-value pairs (e.g., {"name": "Alice", "age": 30}).
- **set**: Used to store a collection of unique items (e.g., {1, 2, 3}).
  Example usage:

```python
x = 10  # int
pi = 3.14  # float
name = "Alice"  # str
is_student = True  # bool
numbers = [1, 2, 3]  # list
coordinates = (10, 20)  # tuple
person = {"name": "Alice", "age": 30}  # dict
unique_numbers = {1, 2, 3}  # set
```

### 5. Arithmetic Operators

Python supports various arithmetic operators that can be used to perform mathematical operations on numbers. Some of the
common arithmetic operators include:

- **+** : Addition
- **-** : Subtraction
- *** : Multiplication
- **/** : Division
- **%** : Modulus (remainder)
- **//** : Floor division (returns the largest integer less than or equal to the result)
- ***** : Exponentiation (raises the left operand to the power of the right operand)
  Example usage:

```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a // b)  # Output: 3
print(a ** b)  # Output: 1000
```

### 6. Comparison Operators

Comparison operators are used to compare two values and return a boolean result (True or False). Some of the common
comparison operators include:

- **==** : Equal to
- **!=** : Not equal to
- **>** : Greater than
- **<** : Less than
- **>=** : Greater than or equal to
- **<=** : Less than or equal to

Example usage:

```python
x = 10
y = 20
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: False
print(x < y)  # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True
```

### 7. Logical Operators

Logical operators are used to combine multiple conditions and return a boolean result. The common logical operators
include:

- **and** : Returns True if both conditions are true
- **or** : Returns True if at least one condition is true
- **not** : Returns True if the condition is false

Example usage:

```python
x = 10
y = 20
print(x > 5 and y < 30)  # Output: True
print(x > 15 or y < 30)  # Output: True
print(not (x > 5))  # Output: False
```

### 8. Assignment Operators

Assignment operators are used to assign values to variables. They can also be combined with arithmetic operators to
perform operations and assign the result to the variable. Some of the common assignment operators include:

- **=** : Assigns a value to a variable
- **+=** : Adds a value to the variable and assigns the result to the variable
- **-=** : Subtracts a value from the variable and assigns the result to the variable
- ***=** : Multiplies the variable by a value and assigns the result to the variable
- **/=** : Divides the variable by a value and assigns the result to the variable
- **%=** : Takes the modulus of the variable by a value and assigns the result to the variable
- **//=** : Takes the floor division of the variable by a value and assigns the result to the variable
- ****=** : Raises the variable to the power of a value and assigns the result to the variable

Example usage:

```python
x = 10
x += 5  # x is now 15
x -= 3  # x is now 12
x *= 2  # x is now 24
x /= 4  # x is now 6.0
x %= 5  # x is now 1.0
x //= 2  # x is now 0.0
x **= 3  # x is now 0.0
```

### 9. Identity Operators

Identity operators are used to compare the memory locations of two objects. The common identity operators include:

- **is** : Returns True if both operands refer to the same object in memory
- **is not** : Returns True if both operands do not refer to the same object in memory

Example usage:

```python
x = [1, 2, 3]
y = x  # y refers to the same list as x
z = [1, 2, 3]  # z is a different list with the same contents
print(x is y)  # Output: True
print(x is z)  # Output: False
print(x is not z)  # Output: True
```

### 10. Membership Operators

Membership operators are used to test whether a value is present in a sequence (such as a list, tuple, or string). The
common membership operators include:

- **in** : Returns True if the value is found in the sequence
- **not in** : Returns True if the value is not found in the sequence

Example usage:

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
print(6 not in my_list)  # Output: True
```

### 11. Bitwise Operators

Bitwise operators are used to perform bit-level operations on integers. The common bitwise operators include:

- **&** : Bitwise AND
- **|** : Bitwise OR
- **^** : Bitwise XOR
- **~** : Bitwise NOT
- **<<** : Left shift
- **>>** : Right shift

Example usage:

```python
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print(x & y)  # Output: 1 (In binary: 0001)
print(x | y)  # Output: 7 (In binary: 0111)
print(x ^ y)  # Output: 6 (In binary: 0110)
print(~x)  # Output: -6 (In binary: 1010)
print(x << 1)  # Output: 10 (In binary: 1010)
print(x >> 1)  # Output: 2 (In binary: 0010
```

### 12. Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. In Python, the operator
precedence is as follows (from highest to lowest):

1. Parentheses `()`
2. Exponentiation `**`
3. Unary plus and minus `+x`, `-x`
4. Multiplication, division, modulus, floor division `*`, `/`, `%`, `//`
5. Addition and subtraction `+`, `-`
6. Bitwise shift operators `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`
11. Identity operators `is`, `is not`
12. Membership operators `in`, `not in`
13. Logical operators `and`, `or`, `not`

Example usage:

```python
result1 = 3 + 4 * 2  # Multiplication is evaluated first, result is 11
result2 = (3 + 4) * 2  # Parentheses are evaluated first, result is 14
```

### 13. Type Conversion

Type conversion is the process of converting a value from one data type to another. In Python, you can perform type
conversion using built-in functions such as `int()`, `float()`, `str()`, etc.

Example usage:

```python
x = "10"
y = int(x)  # Convert string to integer
z = float(x)  # Convert string to float
print(y)  # Output: 10
print(z)  # Output: 10.0
```

**Note**: Refer to [day01_hello.py](../src/basics/day01_hello.py) for the complete code examples.
