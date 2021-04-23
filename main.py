# Ben Bromley NEA project - 2020/21 - Wigston College

from tkinter import *
from tkinter import Tk, messagebox
from tkinter.ttk import *

import databaseManager

# global constants to be implemented when instantiating classes and mainlooping forms
login = Tk()
library = Tk()
# not in use yet
# create = Tk()
# delete = Tk()


# authorises user
# this is called to authorise a user before opening
# and to authorise a user before deleting their account
def auth(username, password):
    """
    :param username:∏
    :param password:
    :return: boolean
    """
    # Converts tkinter variables into python variables
    norm_username = username.get()
    norm_password = password.get()
    # instantiates class
    user_auth_db = databaseManager.UserTable()
    # returns true if login is correct
    return user_auth_db.get_user(norm_username, norm_password)

# TODO: MOVE TO LOGINPAGE CLASS AS A FUNCTION


def auth_to_open(username, password):
    auth_boolean = auth(username, password)
    # opens library if auth_boolean returns true
    if auth_boolean:
        print("Auth returned True")
        login_page_object.close()
        open_library()
    else:
        # TODO: finish warning box work
        messagebox.showwarning("Username and/or password incorrect."
                               "\nPlease Try Again")


# TODO: make create user form
class CreateUserPage:

    # creates the basic tkinter form
    def __init__(self, create_master):
        self.create_master = create_master
        self.create_master.title("Create Account")
        self.create_master.geometry('275x400')  # width then height
        self.create_master.resizable(0, 0)  # cannot resize form
        self.create_master['bg'] = 'light grey'


# TODO: open delete user form
# should require authentication
class DeleteUserPage:

    # creates the basic tkinter form
    def __init__(self, delete_master):
        self.delete_master = delete_master
        self.delete_master.title("Delete Account")
        self.delete_master.geometry('275x400')  # width then height
        self.delete_master.resizable(0, 0)  # cannot resize form
        self.delete_master['bg'] = 'light grey'


# Login page
class LoginPage:
    #  sets up basic form properties
    def __init__(self, master):
        self.master = master
        master.title("Welcome")  # names the form
        self.master.geometry('275x400')  # width then height
        self.master.resizable(0, 0)  # cannot resize form
        # intro label
        self.Top_Lbl = Label(self.master, text="Sign in") \
            .grid(column=0, row=2, padx=(0, 0), pady=(15, 10))

        # region Login Labels
        # Label is below the top label, and above the appropriate entry box
        self.User_Lbl = Label(self.master, text="Username:", anchor='w')\
            .grid(sticky='w', column=0, row=3, padx=(20, 0), pady=(10, 0))
        self.Pass_lbl = Label(self.master, text="Password:", anchor='w')\
            .grid(sticky='w', column=0, row=5, padx=(20, 0), pady=(10, 0))
        # endregion

        # region Username var assignment & entry box
        self.Username = StringVar()
        self.User_Ent = Entry(self.master, width=25, textvariable=self.Username)\
            .grid(column=0, row=4, padx=(20, 0))
        # endregion

        # region Password var assignment & entry box
        self.Password = StringVar()
        self.Pass_Ent = Entry(self.master, width=25, textvariable=self.Password)\
            .grid(column=0, row=6, padx=(20, 0))
        # endregion

        # region button & commands
        self.LoginButton = Button(self.master, text="Login",
                                  command=lambda: [auth_to_open(self.Username, self.Password)])\
            .grid(column=0, row=7, pady=(10, 5))

        self.OptionLabel = Label(self.master, text="Or:").grid(
            column=0, row=8, padx=10, pady=20)

        self.CreateButton = Button(self.master, text="Create a new account",
                                   command=lambda: [LoginPage(master).close(),
                                                    """should open create user form"""]) \
            .grid(column=0, row=9, pady=(5, 5))
        self.DeleteButton = Button(self.master, text="Delete your account",
                                   command=lambda: [LoginPage(master).close(),
                                                    """should open delete user form"""])\
            .grid(column=0, row=10, pady=(5, 5))
        # endregion

    def close(self):
        self.master.destroy()


def open_library():
    library_form_object = PersonalLibrary(library)
    library.mainloop()


class PersonalLibrary:

    def __init__(self, library_master):
        self.library_master = library_master
        self.library_master.title("My Library")  # names the form
        self.library_master.geometry('600x360')  # width then height
        self.library_master.resizable(0, 0)  # cannot resize form

        # region adds main buttons
        self.ImportButton = Button(self.library_master, text="Import File",
                                            command=lambda: self.import_file()).pack()
        self.ExportButton = Button(self.library_master, text="Export File",
                                   command=lambda: self.export_file()).pack()
        # endregion

    def import_file(self):
        # how do I import files?
        return

    def export_file(self):
        # how do I export files?
        return

    # TODO: needs methods to deal with items


# used to open the login page
login_page_object = LoginPage(login)  # instantiates the LoginPage
login.mainloop()  # keeps form running

# output after program closes
print("program finished")

