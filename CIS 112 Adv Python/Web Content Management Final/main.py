"""
Components:
1. Content Editing UI (20 Points)
Your app will include a GUI application that can read in and modify the text of
a webpage you will want to to publish.

2. Static Data Storage (10 Points)
You will create a module to retrieve and edit a static file (exp: a JSON file).
This will serve as static storage for your app. Anytime your user edits the
content via the GUI the update should be stored in the JSON file.

3. Webpage Creation (10 Points)
Whenever your user edits content, the app should also publish a static webpage
file with the revised content, overwriting previous drafts of the site. Make a
module that does this and have the GUI import it as part of the operations of
the app.

4. Server File Hosting (20 Points)
You should independently run a webserver that will send the webpage file to any
client that requests it. Users should be able to navigate to the host location
via a browser and load the webpage on demand.

5. Class and Module Construction (5 Points)
You will employ classes and modules to construct the various elements of your
application. """

#  clickin submit should result in rewritinh the html file, and updating your
#  external json file
import editorgui as app

# initial call to display the gui
app.display()

# calls to acquire user input should be done in... databackend.py(writes JSON
# file)?
# databackend.update_content()??

# after updates, a call to redisplay the information should be called
# app.display?? within a while true loop
