"""

Objective:
Your task is to develop an ordering kiosk application using the Tkinter library in Python. The application should allow customers to enter their name, choose whether to add a drink to their order, select an entree from the provided options, and display their order details upon submission. Utilizing a theme for the application is optional but will earn extra credit.

Requirements:
Create an `OrderingKiosk` class that represents the application.
The application should have the following features:
Entry widget for customers to enter their name. 
Checkbutton to allow customers to choose whether to add a drink to their order
Combobox with options for entrees (e.g., Pizza, Burger, Salad)
Button to submit the order  
Label to display the order details upon submission.
Display the order details, including the customer's name, drink choice (if selected), and selected entree, upon clicking the submit button.
Implement proper error handling to display a message if the customer's name is not provided or if no entree is selected upon submission.
Rubric:
- Class Structure (2 points):
  - Properly define the `OrderingKiosk` class with all necessary methods and attributes.
- Widget Functionality (4 points):
  - Entry widget captures customer name.
  - Checkbutton allows customers to choose whether to add a drink to their order.
  - Combobox provides options for selecting an entree.
  - Button triggers the submission of the order and displays order details.
- Error Handling (2 points):
  - Proper error message is displayed if the customer's name is not provided upon submission.
  - Proper error message is displayed if no entree is selected upon submission.
- Code Quality (2 points):
  - Code is well-structured, organized, and easy to understand.
  - Proper use of Tkinter widgets and methods.
  - Comments are included to explain the purpose of major code sections.
- Extra Credit (2 point):
  - Utilization of a theme for the application interface.
"""

import tkinter as tk
import tkinter.font
from tkinter import messagebox, ttk


def display_order():

    return


def add_drink():

    return


entrees = (
    "Pizza",
    "Burger",
    "Salad",
    "Super Deluxe Burger",
    "Giganto Shake",
    "Snazzy Snack",
    "Crinkle Cut Super Fries",
    "Julienne Super Fries",
    "Fancy Avante Burger w/o fries",
    "Traditional Cheeseburger w/ fries",
)


class OrderingKiosk:
    """
    Represents the application
    application should have the above features
    """

    root = tk.Tk()
    name_label = tk.Label(root, text="Enter Your Name:")
    name_entry = tk.Entry(root)

    drink_chkbtn = tk.Checkbutton(root, text="Add A Drink?", command=add_drink)

    entree_combo = ttk.Combobox(root)
    entree_combo["values"] = entrees

    sub_btn = tk.Button(root, text="Submit", command=display_order)

    order = entree_combo.get()

    details_label = tk.Label(root, text=order)
