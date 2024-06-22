""" Marco Aguilar

Module 4 Part 1 Lab

REQUIREMENTS:

    1. Create a GUI application using Tkinter that includes the following
    components:
        - Label prompting the user to enter their name.
        - Entry widget for users to input their name.
        - Label prompting the user to select their preferred language.
        - Combobox (dropdown menu) for users to select their preferred language
          from a list of options (e.g., English, French, Spanish).
        - Button labeled "Greet Me" that, when clicked, generates a personalized
          greeting message based on the user's input.

    2. Implement functionality to display a greeting message based on the user's
    input:
        - When the "Greet Me" button is clicked, the application should generate
          a greeting message that includes the user's name and is displayed in
          the selected language.

    3. Apply styling and formatting to the GUI components to enhance the visual
    appeal of the application:
        - Use appropriate font styles, sizes, and colors for labels, entry
          widgets, combobox, button, and greeting message.  """

import tkinter
import tkinter.font
from tkinter import messagebox, ttk

# set up the root window for your GUI
root = tkinter.Tk()
root.title("Greeting Generator!!!")
root.config(background="black")
root.geometry("800x800")

# variables to control widget height, width, and x-position
widget_width = 300
widget_height = 100
widget_x = 250
main_font = tkinter.font.Font(family="Arial", size=18, weight="bold")

# label and entry widget for the users name
name_label = tkinter.Label(root, text="Enter Your Name: ", font=main_font)
name_label.place(x=widget_x, y=0, width=widget_width, height=widget_height)
name_entry = tkinter.Entry(root, font=main_font)
name_entry.place(x=widget_x, y=widget_height, width=widget_width, height=widget_height)

# iterable tuple of Language choices for the lang_combo Combobox widget
languages = (
    "English",
    "Spanish",
    "French",
    "Chinese",
    "Japanese",
    "German",
    "Russian",
    "Dutch",
    "Hindi",
    "Korean",
)

# label to prompt user to select a language
lang_label = tkinter.Label(root, text="Select Your Preffered Language", font=main_font)
lang_label.place(
    x=widget_x, y=widget_height * 2, width=widget_width, height=widget_height
)

# ttk combo box with values set to the elements in our languages tuple
lang_combo = ttk.Combobox(root, width=20, font=main_font)
lang_combo["values"] = languages
lang_combo.place(
    x=widget_x, y=3 * widget_height, width=widget_width, height=widget_height
)

# list of different greetings whose indeces match the corresponding language in
# our tuple of languages
diff_greets = [
    "Greetings",
    "Saludos",
    "Bonjour",
    "你好",
    "こんにちは",
    "Grüße",
    "Приветствия",
    "Begroetingen",
    "ग्रीटिंi",
    "인사",
]

# creating a Frame and a Message widget to pack inside the frame
greet_frame = tkinter.Frame(root)
greeting = tkinter.Message(greet_frame)


def greet_user():
    """
    Function will unplace, or make dissapear, the frame for the greeting first.
    This is just in case there is a previously created greeting present. Then
    the function will obtain the user chosen values to create a greeting using
    the users chosen language and name. The constructed greeting is then placed.
    """

    # unplace the frame if it has already been placed
    greet_frame.place_forget()

    # obtain user values
    name = name_entry.get()
    choice = lang_combo.get()

    # make sure the user enters a name
    try:
        if name == "":
            raise Warning
    except Warning:
        warning = messagebox.showwarning("No Input!", "\nPlease enter a name.")
        return

    # make sure the user chooses a language
    try:
        if lang_combo.get() not in languages:
            raise Warning
    except Warning:
        warning = messagebox.showwarning("Please make a language selection.")
        return

    # get the index of the chosen language
    counter = 0
    for option in languages:
        if choice == option:
            break
        else:
            counter += 1

    # create message using users choice language and name
    message = f"{diff_greets[counter]}, {name}!"
    greeting.configure(text=message, font="Impact 40 bold")

    # replace the widgets to their respective masters
    greet_frame.place(
        x=widget_x, y=5 * widget_height, width=widget_width, height=2 * widget_height
    )
    greeting.pack()


greet_btn = tkinter.Button(root, text="Greet Me", command=greet_user)
greet_btn.place(
    x=widget_x, y=4 * widget_height, width=widget_width, height=widget_height
)


root.mainloop()
