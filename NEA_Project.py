# HourGlass

# Start with Auth page

from tkinter import *
from tkinter import Tk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3


# checks user input against database and opens relevant library
def auth(username, password):
    """
    :param username:
    :param password:
    :return: null
    """

    authorised = "False"
    # check username and password against database
    db_connect = sqlite3.connect('music_database.db')
    # the command being assigned to be later
    # TODO change sql statement to apply to my database
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    c = db_connect.cursor()
    print("Successfully Connected to SQLite")
    # executes the command specified in the string
    c.execute(sqlite_create_table_query)
    db_connect.commit()
    print("SQLite table created")
    # gets all values from the database
    c.fetchall()
    # closes data base connection
    c.close()

    ''' if username in database:
    return true
    repeat for password '''

    # get_library_id() method should also be implemented here
    if authorised == "True":
        open_library()
    else:
        messagebox.showwarning("Username and/or password incorrect")


def open_library():
    master1 = Tk()
    main_library = PersonalLibrary(master1)
    master1.mainloop()


class LoginPage:

    def __init__(self, master):

        self.master = master
        master.title("Login Page")  # names the form
        master.geometry('300x180')  # width then height
        master.resizable(0, 0)  # cannot resize form
        self.Top_Lbl = Label(master, text="Please Enter Your Details")\
            .grid(column=1, row=0, padx=(10, 10), pady=(15, 10))

        # region Login Labels
        self.User_Lbl = Label(master, text="Username:").grid(column=0, row=1, padx=(10, 1), pady=(10, 10))
        self.Pass_lbl = Label(master, text="Password").grid(column=0, row=2, padx=(10, 1), pady=(10, 10))
        # endregion

        # region Username var assignment & entry box
        self.Username = StringVar()
        self.User_Ent = Entry(master, width=30, textvariable=self.Username).grid(column=1, row=1)
        # endregion

        # region Password var assignment & entry box
        self.Password = StringVar()
        self.Pass_Ent = Entry(master, width=30, textvariable=self.Password).grid(column=1, row=2,)
        # endregion

        # region button & commands
        self.Submit = Button(master, text="Login",
                             command=lambda: [LoginPage(master).close(),
                                              auth(self.Username, self.Password)]).grid(column=1, row=5,)
        # endregion

    def close(self):
        self.master.destroy()


class PersonalLibrary:

    def __init__(self, master1):

        self.master1 = master1
        master1.title("My Library")  # names the form
        master1.geometry('600x360')  # width then height
        master1.resizable(0, 0)  # cannot resize form


root = Tk()  # runs form
LogPag = LoginPage(root)  # instantiates the LoginPage
root.mainloop()  # keeps form running

# then menu
# then open pdf
