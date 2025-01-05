

numbers_input = input("Enter the numbers separated by spaces: ")

# Split the input string into a list of individual numbers
numbers_list = numbers_input.split()

# Convert each element in the list to an integer
try:
    numbers = [int(num) for num in numbers_list]
    print("Numbers:", numbers)
except ValueError as e:
    print("Error:", e)

def even_odd():
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")

even_odd()

#if a function return type is not specified it returns None
    #we can specify the return type of a function using the -> syntax
    #syntax: def function_name() -> return_type:
    #return_type - type of value returned by the function
    #return statement is used to return a value from a function
    #syntax: return value
    #value - value to return from the function
    #return statement can be used to return multiple values from a function
    #syntax: return value1, value2

def add(a: int, b: int) -> int:
    return a + b
