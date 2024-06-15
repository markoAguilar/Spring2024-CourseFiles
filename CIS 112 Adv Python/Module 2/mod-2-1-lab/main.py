"""
Module 2: Classes and Object-Oriented Programming

Part 1: Programming an ATM using Classes

This program will serve to both test your ability to generate and utilize basic
classes as well as some more advanced uses of the dictionary datatype.
Conduct unit tests on the individual class methods as well check the overall
program output. Ensure it runs properly, including attributes and methods, as
well as modify some of the logic for the overall ATM code to handle some of the
branching conditions.
"""

# OS library to clear terminal (like in tictactoe)
# We use time to keep info on the screen before recycling the program
import os
import time


class BankAccount:
    def __init__(self, holder, balance=0):
        """
        Constructor method: Initializes the instance of BankAccount with arguments
        holder {str} and balance {int}. Balance will have a value of 0 if no
        amount is given

        Arguments:
        holder {str}: the name of the account holder
        balance {int}: the amount to initialize the account balance with

        Returns: instance
        """
        self.account_holder = holder
        self.balance = balance

    def deposit(self, amount):
        """
        Method: will process when a user deposits funds into their account. The
        method takes an amount and adds it to the BankAccount balance.

        Arguments:
        amount {int}: the amount to add to self.balance
        """
        if amount < 0:
            print("Invalid deposit amount. Please enter a positive amount")
            return
        else:
            self.balance += amount

    # method to handle withdrawls including validation checks
    def withdraw(self, amount):
        """
        Method: processes when the user makes a withdrawal. The function will
        take an amount {int} given and subtract(withdraw) the amount from the
        current self.balance

        Arguments:
        amount {int}: valid if positive number and is less than the current
        balance amount
        """
        if amount < 0:
            print("Invalid withdrawal amount. Please enter a positive amount")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            self.balance -= amount

    def get_balance(self):
        """Returns self.balance"""
        return self.balance

    def display_account_info(self):
        """prints the account information"""
        print(f"Account Name: {self.account_holder}")
        print(f"Account Balance: {self.balance}")


def main():
    # Create new dictionary to hold accounts
    accounts = dict()

    # While true to run continuous loop
    while True:
        os.system("clear")

        # User option to create new acocunt or access existing
        print("Welcome to PCC Bank\n     ---ATM---      \n===================")
        print(
            "\nTo create a new account enter 'c'\nTo access an existing :account enter 'a'"
        )
        userselection = input()

        # user inputs new account attributes
        if userselection == "c":
            os.system("clear")
            account = input("Please input the new account holders name: ")
            pin = int(input("Please enter a 4-digit pin: "))
            deposit = int(input("Choose an initial deposit amount: "))

            # Cool thing is here! We create the account as an object stored in
            # the dictionary with the key as the pin. We then use this to lookup
            # or access the account later
            accounts.update({pin: BankAccount(account, deposit)})
            " accounts[pin] = BankAccount(account, deposit)"
            os.system("clear")
            print("Account creation successful!")
            accounts[pin].display_account_info()
            print("Goodbye!")
            time.sleep(5)
        # Here we have the user input a pin. IF it matches a dict key, return
        # the associated account. Otherwise exit
        elif userselection == "a":
            os.system("clear")
            userpin = int(input("To login, please enter your pin: "))
            """TO-DO: Complete the following IF statement logic to check if a pin (and associated account) exists"""
            if pin not in accounts:
                os.system("clear")
                print("Invalid PIN. Goodbye")
                time.sleep(5)
            # Here user will view their current info, and make either a deposit
            # or withdrawl
            else:
                os.system("clear")
                print("Welcome Back!")
                accounts[userpin].display_account_info()
                print("-------")
                userselection = input(
                    "To make a deposit enter 'd'\nTo make a withdrawal enter 'w': "
                )
                if userselection == "d":
                    os.system("clear")
                    deposit = int(input("Enter deposit amount: "))
                    accounts[userpin].deposit(deposit)
                    os.system("clear")
                    print("transaction successful!")
                    accounts[userpin].display_account_info()
                    print("Goodbye!")
                    time.sleep(5)
                elif userselection == "w":
                    os.system("clear")
                    deposit = int(input("Enter withdrawl amount: "))
                    accounts[userpin].withdraw(deposit)
                    os.system("clear")
                    accounts[userpin].display_account_info()
                    print("Goodbye!")
                    time.sleep(5)
        elif userselection == "q":
            return


main()
