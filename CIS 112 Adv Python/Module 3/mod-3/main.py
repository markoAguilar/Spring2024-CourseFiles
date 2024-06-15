import pickle

# Sample problem: Storing information about books
books_info = {
    "001": {"title": "Python Programming", "author": "John Doe", "year": 2020},
    "002": {"title": "Data Science Essentials", "author": "Jane Smith", "year": 2019},
    "003": {
        "title": "Web Development with Flask",
        "author": "Alex Johnson",
        "year": 2021,
    },
}


# function here
def pickle_data(data, filename):
    try:
        # handle file not found exception by simply attempting to open
        fileout = open(filename, "w")

        # handle the data to confirm it is a dictionary
        if not type(data) is dict:
            raise

    except:
        return "An error occurred while pickling the data."

    else:
        # convert the data into a serialized byte string
        serial_books = pickle.dumps(data)
        print("Serial Books: ", serial_books)

        # open the file to write to with the given filename and write the pickled
        # data to that file (convert to str first), don't forget to close the file!
        fileout.write(str(serial_books))
        print("Serial Books: ", serial_books)
        fileout.close

        filein = open(filename, "r")
        print("File Content: ", filein.read())

        return "Data pickled successfully to 'books_data.pickle'"


# Pickle the data
pickle_filename = "books_data.pickle"

assert (
    pickle_data(books_info, pickle_filename)
    == "Data pickled successfully to 'books_data.pickle'"
)
pickle_data(pickle, pickle_filename)
assert (
    pickle_data(pickle, "pickle_filename.pickle")
    == "An error occurred while pickling the data."
)

print("Exercise 1 is correct.")
