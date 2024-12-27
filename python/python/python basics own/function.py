

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

