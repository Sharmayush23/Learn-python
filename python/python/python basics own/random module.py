import random

# Generate a list of 10 random integers between 1 and 100
random_integers = [random.randint(1, 100) for _ in range(10)]
print(random_integers)


# List of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Number of random fruits to choose
number_of_fruits = 3

# Choose multiple random fruits (can include duplicates)
random_fruits = [random.choice(fruits) for x in range(number_of_fruits)]
print("Random fruits:", random_fruits)
words = ["apple", "banana", "cherry"]

# Extract the first letter of each word
first_letters = [word[0] for word in words]

print(first_letters)
