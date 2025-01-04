

# 2. Strings

# Creating Strings:
# Use single quotes ('...'), double quotes ("..."), triple single quotes ('''...'''), or triple double quotes ("""...""").
# Single/double quotes for single-line strings.
# Triple quotes for multi-line strings.
# Type conversion using str().
# Example:
string1 = 'hello'
string2 = "world"
string3 = '''This is a
multi-line string'''
string4 = str(123)

# Indexing: Access individual characters by position.
# Positive indexing: Starts from 0 (left to right).
# Negative indexing: Starts from -1 (right to left).
# Example:
s = "Hello"
print(s[0])  # Output: H
print(s[-1]) # Output: o

# Slicing: Extract substrings.
# Syntax: string[start:end:step]
# start: Starting index (inclusive).
# end: Ending index (exclusive).
# step: Step size.
# Examples:
s = "Hello World"
print(s[0:5])    # Output: Hello
print(s[6:])    # Output: World
print(s[::2])   # Output: HloWrd
print(s[::-1])  # Output: dlroW olleH (Reversed string)
# If step is negative, the start index should be greater than the end index.

# Immutability: Strings are immutable (cannot be changed after creation). Operations like capitalization create new strings.

# String Operators:
# Arithmetic Operators:
# +: Concatenation. Example: "Delhi" + "Mumbai" outputs "DelhiMumbai".
# *: Repetition. Example: "Delhi" * 3 outputs "DelhiDelhiDelhi".
# Relational Operators:
# Compare strings lexicographically (like dictionary order). Capital letters are considered smaller than small letters.
# Examples: >, <, ==, !=, >=, <=
# Logical Operators:
# and, or, not.
# Non-empty strings are considered True, empty strings are False.
# and returns the first false value or the last true value; or returns the first true value or the last false value.
# Looping: Strings can be iterated.
# Example:
for char in "Delhi":
    print(char)
# Membership Operators:
# in, not in: Check if a substring exists. Example: "Delhi" in "New Delhi" returns True.

# String Functions:
# Common Functions:
# len(): Returns the length of the string.
# max(): Returns the character with the maximum value based on Unicode.
# min(): Returns the character with the minimum value based on Unicode.
# sorted(): Returns a list of characters sorted in ascending order.
# String-Specific Functions:
# capitalize(): Capitalizes the first character.
# title(): Converts to title case (first letter of each word capitalized).
# upper(): Converts to uppercase.
# lower(): Converts to lowercase.
# count(): Counts occurrences of a substring.
# find(): Returns the index of the first occurrence of a substring, or -1 if not found.
# index(): Returns the index of the first occurrence of a substring or raises an error if not found.
# startswith(): Checks if the string starts with a specific substring.
# endswith(): Checks if the string ends with a specific substring.
# format(): Formats a string by inserting values into placeholders.
# isalnum(): Checks if all characters are alphanumeric.
# isalpha(): Checks if all characters are alphabetic.
# isidentifier(): Checks if the string is a valid identifier.
# split(): Splits the string into a list of substrings based on a delimiter, which defaults to spaces.
# join(): Joins a list of strings into one string using a separator string.
# replace(): Replaces all occurrences of a substring with another string.
# strip(): Removes leading/trailing whitespace.

# 3. Other important points:

# Unicode: Python uses Unicode for strings, supporting diverse characters.
# Mutable vs. Immutable Data Types: Strings are immutable. Operations that seem to modify strings actually create new ones.
# Practice: Coding and understanding code is crucial for learning.
# Problem Solving: Break down complex problems into smaller parts.

# strings working with the textual data
message = "hellp booby"
print(message)
name = 'ayush"ayu"'
print(name)
print(len(message))
print(len(name))
# slicing
print(name[0:3])
print(name[-10:-1])
print(message.casefold())
print(message.find('ayu'))
print(name.find('ayu'))

greeting = "namaste"
name = "gagandeep"
# concatenation
mess = greeting + ' ' + name
print(mess)
age = 25
# f strings formatting
mess2 = f" hello my name is {name.upper()} and i am {age} years old"
print(mess2)
# formatting using format methods
mess3 = '{} ,{} . your age is {}'.format(name, greeting, age)
print(mess3)
# print(dir(name))
print("\n")
# print(help(str))

name = "ayush"
print(name.upper())
print(name.capitalize())
print(message.casefold())
