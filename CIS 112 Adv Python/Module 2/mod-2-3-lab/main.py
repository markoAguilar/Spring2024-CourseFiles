# Module 2 part 3.

# Variable to track your progress and score you on this assignment
total_score = 0

"""Exercise 1
Create a function 'meatball' that takes no inputs and prints:
"I lost my poor meatball, when somebody sneezed!"

We then define a wrapper function 'spaghetti' that takes in a function
as an input, prints: "On top of spaghetti, all covered in cheese."
and ends on the same line (end=' ') then invokes the function input
to complete the song.

Make sure to decorate meatball with the shorthand spaghetti wrapper.
"""


def spaghetti(func):
    def wrapper():
        print("On top of spaghetti, all covered in cheese.", end=" ")
        func()

    return wrapper


@spaghetti
def meatball():
    print("I lost my poor meatball, when somebody sneezed!")


# Invoke meatball
meatball()
print("Exercise 1 is correct.")
total_score += 2

####

"""Exercise 2
Modify your meatball function to take in an input 'food' that modifies the output string
to "I lost my poor {food}, when somebody sneezed!" and then modify the wrapper function
to take in a flexible amount of arguments (*args)
"""


def meatball(food):
    print(f"I lost my poor {food}, when somebody sneezed!")

    def spaghetti(*args):
        print("On top of spaghetti, all covered in cheese.", end=" ")

    return spaghetti


# Invoke Meatball again
meatball("hotdog")

print("Exercise 2 is correct.")
total_score += 2

####

"""Exercise 3
Modify your previous meatball wrapped function to be a class method for a class
'Song'. I should be able to create a song object and then invoke the object.meatball('food')
method to handle individual food items.
"""


def meatball(food):
    print(f"I lost my poor {food}, when somebody sneezed!")

    @classmethod
    def spaghetti(*args):
        print("On top of spaghetti, all covered in cheese.", end=" ")

    return spaghetti


# create a Song object then invoke it!
pizza = Song()
pizza.meatball("Pizza")
print("Exercise 3 is correct.")
total_score += 2

####

""" Exercise 4
Define a class 'MathUtils', that includes a static method 'add' that adds two
inputs 'x' and 'y' together and returns the result.
"""


# Invoke the static method
result = MathUtils.add(3, 5)
print(result)  # Output: 8

print("Exercise 4 is correct.")
total_score += 2

####

""" Exercise 5
We'll now create a class-level method. They are often used as alternative
constructors or to access or modify class-level attributes.

First create a class 'Customer'. Customer will:
  - have a class-level attribute 'count' that will be initialized to 0
  - a constructor that defines an object attribute 'name' based on an input AND
    also increments the Customer.count attribute by 1 (the idea behind this is every)
    time an object of the class is constructed, the overall count goes up by 1.
  - Define 'get_count' a class method defined using the @classmethod decorator.
    Class methods take the class itself (cls) as their first argument, allowing
    access to class variables and other class-specific methods. You should return
    the count attribute
"""


# Invoke two examples of customers
obj1 = Customer("Alice")
obj2 = Customer("Bob")

print(Customer.get_count())  # Output: 2

print("Exercise 5 is correct.")
total_score += 2

####

""" Exercise 6
Using our ATM exercise as inspiration create a Class 'Account'.
Account should have 2 private attributes: name, and balance.

The class should provide getter and setter methods:
  - (get_name, set_name, get_balance, set_balance)
to access and modify these private attributes, respectively.

This encapsulation ensures that the attributes can only be accessed or modified
through these methods, allowing for better control and validation of attribute values.

-Create a SavingsAccount class, a subclass of Account, that directly inherits
  the private attributes (no modifications needed).
"""


# Creating an instance of the Account class
account1 = Account("Alice", 1000)

# Accessing protected attributes using getters
print(account1.get_name())  # Output: Alice
print(account1.get_balance())  # Output: 1000

# Modifying protected attributes using setters
account1.set_name("Bob")
account1.set_balance(2000)

# Accessing protected attributes after modification
print(account1.get_name())  # Output: Bob
print(account1.get_balance())  # Output: 2000

# Creating an instance of the SavingsAccount subclass
savings_account = SavingsAccount("Carol", 1500)

# Accessing inherited protected attributes using getters
print(savings_account.get_name())  # Output: Carol
print(savings_account.get_balance())  # Output: 1500

# Modifying inherited protected attributes using setters
savings_account.set_name("David")
savings_account.set_balance(2500)

# Accessing inherited protected attributes after modification
print(savings_account.get_name())  # Output: David
print(savings_account.get_balance())  # Output: 2500


print("Exercise 6 is correct.")
total_score += 4

####

""" Exercise 6
-Modify your previously defined Account class representing a basic account
  with a name (_name) and balance (_balance) attribute.
  Both attributes should now be protected (denoted by _).


-Modify your SavingsAccount class, a subclass of Account.

- The subclass should now add a new protected attribute, interest_rate, and
  defines its own getters and setters for it.

- The subclass should also have a set_balance() method that when invoked
  modifies the parent class balance using the formula:
  self._balance = balance + (balance * self._interest_rate)  to applying
  the interest rate

"""


# Creating an instance of the SavingsAccount subclass
savings_account = SavingsAccount("Carol", 1500, 0.05)

# Modifying balance directly through the subclass method
savings_account.set_balance()

# Accessing the modified balance attribute
print(savings_account.get_balance())  # Output: 1575.0


print("Exercise 7 is correct.")
total_score += 6

####

# You've reached the end of Lab Exercise 3.
# Your total score for this lab is:
print(f"{(total_score/20)*100}%")
