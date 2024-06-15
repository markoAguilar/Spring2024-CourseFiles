"""
Marco Aguilar
CIS 112: Advanced Python

The following sequence of exercies are designed to help reenforce and strengthen
your understanding of the OOP concepts explored in mod-2-2.pdf
"""


class Employee:
    """
    Class: represents a single employee.

    Attributes:
        Arguments:
            nameIn: the name to be assigned to self.name
        Methods:
    """

    def __init__(self, nameIn):
        self.store = "South Pasadena"
        self.name = nameIn

    def describe(self):
        return f"{self.name} is an employee at the {self.store} location"


# Creating instance of Employee
lancer = Employee("Lancer")
print(lancer.describe())


assert lancer.describe == "Lancer is an employee at the South Pasadena location"
