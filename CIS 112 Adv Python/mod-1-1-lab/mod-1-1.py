import random

"""
This lab assignment is a simple review of the intro skills learned in the
previousPython course!
"""

# Python assertions are code that ensure the program does not continue running
# if the assertion tests are not passed. The message is optional.
fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]
assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"], "List values not as expected"

# appending to a list
fruits.append("tomato")
print(f"\nYour list: {fruits}")

# reversing a list
fruits.reverse()
print(f"\nYour list reversed: {fruits}")

# sorting and then sorting in reverse
fruits.sort()
print(f"\nSorted: {fruits}")
fruits.reverse()
print(f"Reversed after sort: {fruits}")

# adding 2 lists together
vegetables = ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
fruitsVeggies = fruits + vegetables
print(f"\nFruits and Vegetables: {fruitsVeggies}")

# for random numbers you must first import the 'random' library, as seen at the top of this file
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)
positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("\nWe now have some random numbers available for future use!")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)


# It is good practice to include docstrings in functions!
def is_positive(number):
    """
    Input: number, any integer number
    Output: boolean, returns True or False depending on if the number is positive
    """
    if (number > 0):
        return True
    else:
        return False


print(f"\n5 is a positive number: {is_positive(5)}")
print(f"\n-5 is a positive number: {is_positive(-5)}")



print("END")
