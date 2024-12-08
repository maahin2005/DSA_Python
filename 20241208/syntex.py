### 1. Variables and Data Types

# Variable declaration
x = 10         # Integer
y = 3.14       # Float
name = "Mahin" # String
is_active = True # Boolean

# Multi-variable assignment
a, b, c = 1, 2, "Python"

# Type casting
num = int("42")  # Convert string to integer
flt = float("3.14") # Convert string to float

### 2. Input and Output

# Input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Output
print(f"Hello, {name}! You are {age} years old.")

### 3. Conditional Statements

x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


### 4. Loops

# For loop
for i in range(5): # range(5) -> [0, 1, 2, 3, 4]
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

### 5. Functions

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
message = greet("Mahin")
print(message)


### 6. Data Structures

nums = [1, 2, 3, 4]
nums.append(5)        # Add element
nums.remove(2)        # Remove element
nums[1] = 10          # Update element
print(nums)

# Tuples

coords = (10, 20)
# Immutable: can't change elements

# Dictionaries

person = {"name": "Mahin", "age": 18}
person["age"] = 19      # Update value
print(person["name"])   # Access value

# Sets

unique_nums = {1, 2, 3, 3}  # Duplicates are removed
unique_nums.add(4)


### 7. List Comprehensions

squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]


### 8. String Operations

text = "Hello, Python!"
print(text.upper())   # Convert to uppercase
print(text.lower())   # Convert to lowercase
print(text.split(",")) # Split into a list


### 9. Classes and Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}."

person = Person("Mahin", 25)
print(person.greet())


### 10. Exception Handling

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution finished.")


### 11. Lambda Functions

add = lambda a, b: a + b
print(add(2, 3))  # Output: 5


### 12. Modules and Imports

import math
print(math.sqrt(16))  # Output: 4.0


##=>  Important Libraries for DSA

#     NumPy for numerical operations.
#     Pandas for data manipulation.
#     Matplotlib for visualization.
#     Collections for advanced data structures like deque, Counter.
#     Heapq for heap-related problems.