


"""
This script demonstrates the usage of various list methods in Python.

Topics covered:
1. Lists:
    - Definition: Lists are ordered, mutable, and can contain heterogeneous data types.
    - Creating Lists:
      - Empty list: list1 = []
      - Homogenous list: list2 = [1, 2, 3]
      - 2D list: list3 = [[1, 2], [3, 4]]
      - 3D list: list4 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
      - Heterogeneous list: list5 = [1, "oo", 5, 6, 5+6j, "Hello"]
      - Using type conversion: list6 = list("hello")
    - Accessing Items (Indexing and Slicing):
      - Indexing:
         - Positive indexing (starts from 0): list1[0] gets the first item.
         - Negative indexing (starts from -1): list1[-1] gets the last item.
      - Slicing: list1[start:end:step]
         - start: Starting index (inclusive).
         - end: Ending index (exclusive).
         - step: Step size.
         - Example: list1[0:3] gets items from index 0 up to (but not including) 3, list1[-3:] gets the last three items.
         - Reversing a list: list1[::-1].
      - Accessing items in nested lists: use multiple square brackets to access nested items, for example: list4[0][1].
    - Adding Items:
      - append(): Adds an item to the end of the list: list1.append(6).
      - extend(): Adds multiple items from another list to the end of the list: list1.extend([7, 8]).
      - insert(): Inserts an item at a specified index: list1.insert(1, 100).
    - Editing Items:
      - Directly assigning new values using indexing: list1[-1] = 500.
      - Using slicing: list1[1:4] = [10, 20, 30].
    - Deleting Items:
      - del keyword: Can delete the entire list, specific items, or a slice.
         - del list1 deletes the entire list.
         - del list1[0] deletes the first item.
         - del list1[1:3] deletes items from index 1 up to (but not including) 3.
      - remove(): Removes an item by value: list1.remove(5).
      - pop(): Removes and returns an item by index (or the last item if no index is provided): list1.pop(0) or list1.pop().
      - clear(): Removes all items from the list: list1.clear().
    - List Operators:
      - +: Concatenation (merges two lists): list1 + list2.
      - *: Repetition (repeats a list multiple times): list1 * 3.
      - in, not in: Membership operators (check if an item exists in a list).
    - Looping Through Lists:
      - Item-wise loop:
         for item in list1:
              print(item)
      - Index-wise loop:
         for i in range(len(list1)):
              print(list1[i])
    - List Functions:
      - Common functions: len(), min(), max(), sorted().
      - List-specific functions:
         - count(): Counts occurrences of an item: list1.count(2).
         - index(): Returns the index of an item: list1.index(3).
         - reverse(): Reverses the list in place (permanent change): list1.reverse().
         - sort(): Sorts the list in place (permanent change): list1.sort().
         - copy(): Creates a shallow copy of the list: list2 = list1.copy().
    - List Comprehension: A concise way to create lists.
      - Syntax: [expression for item in iterable if condition].
         - Example: [i for i in range(1, 11)] creates a list of numbers from 1 to 10.
         - With a condition: [i for i in range(1, 51) if i % 5 == 0] creates a list of numbers from 1 to 50 that are divisible by 5.
         - Nested list comprehension: [[1 for j in range(3)] for i in range(3)] creates a 2D matrix.
    - Zip Function: Used to combine multiple lists element-wise.
      - Syntax: zip(list1, list2)
      - Returns a zip object (an iterator of tuples). You can convert the zip object to a list using list(zip(list1, list2)).
      - Example:
         list1 = [1, 2, 3]
         list2 = [4, 5, 6]
         zipped_list = list(zip(list1, list2))  # Output: [(1, 4), (2, 5), (3, 6)]

2. Important Considerations:
    - Dynamic Arrays: Lists act like dynamic arrays and can grow or shrink as needed, but this can lead to slower execution and more memory usage.
    - Referential Arrays: Lists store references (pointers) to objects, not the actual objects themselves. This allows lists to store different data types, but requires more memory and time for access.
    - Mutable: Lists are mutable (can be changed after creation).
      - When you copy a list without using the copy() method, the new list is referencing the original one. This can cause changes in one list to reflect in the other, which can lead to unexpected results.
    - Python Objects: Lists can store any kind of Python object, including functions and classes.
    - Homogeneous vs. Heterogeneous:
      - Homogeneous lists contain items of the same data type.
      - Heterogeneous lists can store items of different data types.

"""

#muttable so it can be change"""
#return the same list with changes
#strings are immuttable
l1=[3,4,5,2,5,2]
print(type(l1))
print("list:",l1)
l1.sort()
print(l1)
# there is a list of all the attributes and methods of the list
#dir(list)
#help(list)
#help(list.sort) list.sort is a method of list class 
#help(list.append) append is a method of list class 
#help(list.pop)  pop is a method of list class
#help(list.remove) remove is a method of list class
#help(list.reverse) reverse is a method of list class
#help(list.insert) insert is a method of list class
#help(list.count)   count is a method of list class
#help(list.extend) extend is a method of list class
#help(list.index) index is a method of list class
#help(list.copy) copy is a method of list class
#help(list.clear) clear is a method of list class
