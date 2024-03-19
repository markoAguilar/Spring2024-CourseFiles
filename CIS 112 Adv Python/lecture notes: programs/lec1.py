num1 = int(input())
num2 = int(input())

sum = num1 + num2

print(f"The sum of these numbers is {sum}")

"""Triple quotes for comment blocks"""

# single quotes for lines of comment

"""
Python is a dynamically typed language.
"""

# you can add strings together
myPhrase = "hel" + "lo"
print(f"Adding hel and lo gives you {myPhrase}")

# there are many ways to 'escape' characters
# you can use a backslash for an apostrophe \'
# or you can specify a string with double quotes instead

print(f"Adding Hel and lo gives you {'Hel'+'lo'}")
print(f"Mike's Books. Joseph's Llamas")

"""
Referentiability vs. Mutability

"""

# Lists are defined with brackets [] with individual values
# separated by commas. They are indexable or referentiable
nums = [1, 2, 3, 4]

print(f"The value at index 3 is {nums[3]}")

# Tuples are another form of a list except they are immutable
# these are declared similarly but with Parenthesis
myTup = (3, 4, 5, 6)
print(f"The value at index 0 is {myTup[0]}")

# The lease useful from of lists are sets which are defined
# with curly brackets {}. They are unordered

"""
Dictionaries are another useful type of list. It has a key and a value and are also declared with curly brackets {}

You can have a key be a username string and the value be yet
another dictionary with more keys and values!!

Furthermore since python is dynamically typed, each key or
value can be of a different type in the same dictionary.
However, this may cause run-time errors depending on how you
are using the dictionary! 
"""
thisDict = {"key1": 45, "key2": 55, "key3": 78}
print("Enter key1, key2, or key3 to see its value")
key = input()
print(f"The value at key {key} is {thisDict[key]}")

"""
CONTROL FLOW (if, elif, else, while loops, for loops)
"""
temp = 54

if temp < 72:
    print("run heat")
elif temp > 82:
    print("run AC")
else:
    print("chill")

while temp < 72:
    print("Running heat")
    temp += 2

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num**2)

for i in range(0, len(numbers)):
    print(numbers[i] ** 2)

"""
for loops:
- have a known number of iterations
- can end early via a break
- uses a counter
- can rewrite a for loop using a while loop

while loops:
-
-
"""
for i in range(1, 20, 2):
    print(i)

counter = 1
while counter < 11:
    print(f"counter in while loop: {counter}")
    counter += 1

# you CAN set the range arbitrarly high to sort of make a
# pseudo while loop and just check the counters value
# then just break out of the loop
for i in range(1, 10000000):
    print(i)
    if i > 10:
        break
"""
breaks will break only out of the current loop. So you can have
multiple breaks in a loop with other loops. This comes in handy
in several different use cases.

Additionally, there is also the continue statement. The continue
statement __________
"""

# student q: what if you want to keep track of how may times
# you ran a loop?
temp = 45
counter = 0

while temp < 72:
    temp += 2
    counter += 1

print(f"this ran {counter} times")
