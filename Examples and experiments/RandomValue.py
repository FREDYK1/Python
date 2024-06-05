import random

lower_range = int(input("Enter the least value: "))
highest_range = int(input("Enter the highest value: "))

random_number = random.randrange(lower_range, highest_range + 1)

print(f"A random number between {lower_range} and {highest_range} is {random_number}")
