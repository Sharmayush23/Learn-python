
#input method is used for the user input means the user can give the input to the program
#then user can work on the input given by the user


#we can take the input from the user using the input method 
#syntax of the input method is 
#variable_name=input("message to the user") 
#variable_name is the variable in which the input given by the user is stored
#message to the user is the message that is displayed to the user
#the input method always returns the string value
#by defoult the input method always returns the string value

# --- 1. Basic Operations ---
# Store Input: Allows the user to input a value, which is stored in a variable for later use.
# Example: User inputs their name.
name = input("Enter your name: ")
print("Hello,", name)

# Multiple Inputs: Takes multiple pieces of input separated by spaces.
# Example: User enters two numbers.
x, y = input("Enter two numbers: ").split()
#.split() method is used to split the input given by the user accoriding to the spaces you can also split the input given by the user according to the other delimeter
print(x, y)

# Type Conversion: Converts the input from string to integer or float for arithmetic or comparisons.
# Example: User inputs their age (integer) and height (float).
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# --- 2. String Manipulations ---
# Concatenation: Combines input with another string.
# Example: Combine user-provided last name with a default first name.
last_name = input("Enter your last name: ")
full_name = "John " + last_name
print(full_name)

# Case Transformations: Converts the input to uppercase, lowercase, etc.
# Example: Convert input to uppercase.
data = input("Enter something: ").upper()
print(data)

# Trimming Spaces: Removes leading and trailing spaces from input.
# Example: Input with extra spaces.
trimmed = input("Enter something with spaces: ").strip()
print(trimmed)

# Search and Replace: Replaces specific substrings within the input.
# Example: Replace "bad" with "good" in the input sentence.
modified = input("Enter a sentence: ").replace("bad", "good")
print(modified)

# --- 3. Splitting and Joining Strings ---
# Split Input: Splits the input string into a list based on spaces or other delimiters.
# Example: User inputs words separated by spaces.
words = input("Enter words separated by space: ").split()
print(words)

# Join Strings: Joins a list of strings into one string with a specified delimiter.
# Example: Join words with a hyphen (-).
joined = "-".join(input("Enter words separated by space: ").split())
print(joined)

# --- 4. Validation and Error Handling ---
# Validate Input: Checks whether the input matches a condition (e.g., numeric or alphabetic).
# Example: Verify input type.
data = input("Enter something: ")
if data.isdigit():
    print("You entered a number.")
elif data.isalpha():
    print("You entered text.")

# Exception Handling: Handles incorrect inputs gracefully using try-except blocks.
# Example: Convert input to an integer, with error handling.
try:
    number = int(input("Enter an integer: "))
    print("Your number is", number)
except ValueError:
    print("That is not an integer!")

# --- 5. Mathematical Operations ---
# Perform Arithmetic: Perform calculations with user input.
# Example: Add two numbers.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum is:", x + y)

# Create Lists or Tuples: Convert input into a list of numbers.
# Example: User enters numbers separated by spaces.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(numbers)

# --- 6. Conditional Input Handling ---
# Ask Until Valid Input: Repeatedly ask the user for valid input until conditions are met.
# Example: Accept only positive numbers.
while True:
    num = input("Enter a positive number: ")
    if num.isdigit() and int(num) > 0:
        break
    print("Invalid input, try again!")
print("Valid input:", num)

# --- 7. Advanced Data Structures ---
# Nested Data Input: Accept multi-line input for a matrix or nested lists.
# Example: User inputs rows of a matrix.
matrix = []
rows = int(input("Enter number of rows: "))
for _ in range(rows):
    matrix.append(list(map(int, input().split())))
print(matrix)

# Dictionaries: Parse key-value pairs from user input.
# Example: Create a dictionary from input.
key_value = input("Enter key:value pairs separated by space: ").split()
dictionary = {k: v for k, v in (pair.split(":") for pair in key_value)}
print(dictionary)

# --- 8. Simulating User Choices ---
# Menu-based Input: Display options and let the user select one.
# Example: Simple calculator menu.
print("Menu:")
print("1. Add")
print("2. Subtract")
choice = input("Choose an option: ")
if choice == '1':
    print("Add chosen!")
elif choice == '2':
    print("Subtract chosen!")
else:
    print("Invalid choice!")

# --- 9. Using Regular Expressions ---
# Pattern Matching: Validate or parse input using regex.
# Example: Check for a valid email address.
import re
data = input("Enter email: ")
if re.match(r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', data):
    print("Valid email!")
else:
    print("Invalid email!")

# --- 10. File or Data Saving ---
# Save Input to a File: Write user-provided data into a file.
# Example: Save a string to a file called "output.txt".
with open("output.txt", "w") as file:
    file.write(input("Enter data to save: "))
