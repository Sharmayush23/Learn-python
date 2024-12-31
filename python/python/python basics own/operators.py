# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
#Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Logical Operators:
  # and give true if both the conditions are true
  # or give true if any one of the conditions is true 
  # not  give the opposite of the condition

# Membership Operators:
   # in  give true if the value is in the iterable 
   # not in
# Logical Operators:
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# Membership Operators:
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)     # True
print(6 in my_list)     # False
print(3 not in my_list) # False
print(6 not in my_list) # True

# Identity Operators:
# is: returns True if both variables are the same object
# is not: returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)       # True
print(x is y)       # False
print(x == y)       # True
print(x is not z)   # False
print(x is not y)   # True
print(x != y)       # False

# Bitwise Operators:
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Zero fill left shift), >> (Signed right shift)
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print(a & b)  # 0 (0000 in binary)
print(a | b)  # 14 (1110 in binary)
print(a ^ b)  # 14 (1110 in binary)
print(~a)     # -11 (inverts all the bits)
print(a << 2) # 40 (101000 in binary)
print(a >> 2) # 2 (10 in binary)