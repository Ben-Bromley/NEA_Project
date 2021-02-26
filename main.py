# Ben Bromley NEA project - 2020/21 - Wigston College

from tkinter import *
from tkinter import Tk, messagebox
from tkinter.ttk import *

import databaseManager


# authorises user
def auth(username, password):
    """
    :param username:∏
    :param password:
    :return: boolean
    """
    # Converts tkinter variables into python variables
    normUsername = username.get()
    normPassword = password.get()
    # Checking new and old variables
    print(normUsername, normPassword)
    print(username, password)
    # instantiates class
    auth_user_object = databaseManager.UserTable()
    # returns true if login is correct
    auth_boolean = auth_user_object.get_user((normUsername), (normPassword))
    # opens library if auth_boolean returns true
    if auth_boolean:
        print("Auth returned True")
        login_page_object.close()
        open_library()
    else:
        # TODO: finish warning box work
        messagebox.showwarning("Username and/or password incorrect."
                               "\nPlease Try Again")
        #


# TODO: make create user form
# def open_create_user():

# TODO: open delete user form
# def open_delete_user():


# Login page

class LoginPage:

    def __init__(self, master):
        self.master = master
        self.master.title("Welcome")  # names the form
        self.master.geometry('275x400')  # width then height
        self.master.resizable(0, 0)  # cannot resize form
        self.master['bg'] = 'light grey'
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
                                  command=lambda: [auth(self.Username, self.Password)])\
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
    main_library = Tk()
    library_form_object = PersonalLibrary(main_library)
    main_library.mainloop()


class PersonalLibrary:

    def __init__(self, main_library):
        self.main_library = main_library
        self.main_library.title("My Library")  # names the form
        self.main_library.geometry('600x360')  # width then height
        self.main_library.resizable(0, 0)  # cannot resize form


# used to open the login page
root = Tk()  # runs form
login_page_object = LoginPage(root)  # instantiates the LoginPage
root.mainloop()  # keeps form running
#
print("running random code")
# then open pdf
