
"""
 List Comprehension: A concise way to create lists.
      - Syntax: [expression for item in iterable if condition].
         - Example: [i for i in range(1, 11)] creates a list of numbers from 1 to 10.
         - With a condition: [i for i in range(1, 51) if i % 5 == 0] creates a list of numbers from 1 to 50 that are divisible by 5.
         - Nested list comprehension: [[1 for j in range(3)] for i in range(3)] creates a 2D matrix.
"""

list=[2,5,6,3,6,16,6]

for i in range(0,8):
    list.append(i)

print(list)
no=[3,4,2,6,7,34]
sq_no=[i**2  for i in no]   
print(sq_no) 
number=[45,4,4,6,3,6,3,5,7,4]

even_numbers=[i for i in number if i%2==0]
print(even_numbers)

string=['4','5','7','7','5']
print(type(string))
numbers=[int(i)  for i in string]
print(numbers)
print(type(numbers))

