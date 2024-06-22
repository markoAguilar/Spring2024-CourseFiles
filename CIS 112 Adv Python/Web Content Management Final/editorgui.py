import json
import tkinter as tk
import tkinter.font
from tkinter import messagebox

import htmlgenerator as htmlgen


def display():
    """
    Function Displays content written to Json File
    """
    # remove the edit frame
    edit_frame.pack_forget()

    # show the display frame
    display_frame.pack()

    # load content from external JSON file to be displayed
    data = {}
    with open(filename, "r") as filein:
        try:
            data = json.load(filein)
        except:
            print("Nothing To Show")

    print(f"Loaded: {data}")

    if len(data) == 0:
        title.config(text="No Title")
        content.config(text="No Content")
    else:
        title.config(text=data["title"])
        content.config(text=data["content"])

    # place all widgets back
    edit_btn.grid(column=0, row=2)

    title_label.grid(column=1, row=1)
    title.grid(column=1, row=2)

    content_label.grid(column=1, row=3)
    content.grid(column=1, row=4)

    # last but certainly not least close the file and call mainloop
    filein.close()
    root.mainloop()


def display_edit():
    """
    Function displays a gui with 2 text entry fields for user input. The inputs
    will be the title and the content of the website.
    """

    # remove the display frame
    display_frame.pack_forget()

    # show the edit frame
    edit_frame.pack()

    title_label_edit.grid(column=1, row=1)
    title_entry.grid(column=1, row=2)

    content_label_edit.grid(column=1, row=3)
    content_input.grid(column=1, row=4)

    sub_btn.grid(column=0, row=2)

    root.mainloop()


def submit():
    """
    Function saves data to Json file and checks that the user has made an input
    on both text entry fields. Function then displays the saved Data to the user
    """
    new_title = title_entry.get("1.0", "end-1c")
    new_content = content_input.get("1.0", "end-1c")

    try:
        if new_title == "" or new_content == "":
            raise ValueError("Empty String")
    except ValueError:
        messagebox.showwarning("No Input", "Please be sure to enter an input")
        return

    update()
    gen_html()
    display()
    return


def update():
    """
    Function gets the data from text entry field and dumps it as json data to an
    external json file named pagecontent.json"""

    new_data = {}
    new_data.update({"title": title_entry.get("1.0", "end-1c")})
    new_data.update({"content": content_input.get("1.0", "end-1c")})
    print(f"Data Added: {new_data}")

    with open(filename, "w") as fileout:
        json.dump(new_data, fileout)
    fileout.close()
    return


def gen_html():
    """
    Function will carry out the creation or modification of the html file"""
    htmlgen.gen_html(
        title_entry.get("1.0", "end-1c"), content_input.get("1.0", "end-1c")
    )


# heigh, width, font for widgets
base_w = 100
base_h = 4
base_font_size = 18
base_backg = "Black"
filename = "pagecontent.json"

# define all widgets to be used
root = tk.Tk()
root.attributes("-fullscreen", True)
display_frame = tk.Frame(root)
edit_frame = tk.Frame(root)

default_font = tkinter.font.Font(family="Impact", size=base_font_size, weight="bold")

# the following are used when display() is called to show the currently saved
# data to the user.
title_label = tk.Label(
    display_frame, text="Title:", height=base_h, width=base_w, background=base_backg
)

content_label = tk.Label(
    display_frame,
    text="Site Content:",
    height=base_h,
    width=base_w,
    background=base_backg,
)

content = tk.Label(display_frame, height=base_h * 6, width=base_w)
title = tk.Label(display_frame, height=base_h // 2, width=base_w)
edit_btn = tk.Button(
    display_frame,
    text="Edit",
    width=2,
    height=3,
    font=default_font,
    command=display_edit,
)

# used when display_edit is called which prompts the user for input
title_label_edit = tk.Label(
    edit_frame, text="Title:", height=base_h, width=base_w, background=base_backg
)

content_label_edit = tk.Label(
    edit_frame,
    text="Site Content:",
    height=base_h,
    width=base_w,
    background=base_backg,
)

content_input = tk.Text(edit_frame, height=base_h * 6, width=base_w)
title_entry = tk.Text(edit_frame, width=base_w, height=base_h // 2)
sub_btn = tk.Button(
    edit_frame, text="Save", width=2, height=3, font=default_font, command=submit
)
