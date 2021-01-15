# Ben Bromley NEA project - 2020/21 - Wigston College

from tkinter import *
from tkinter import Tk
from tkinter.ttk import *
from tkinter import messagebox
import Database_Manager


# authorises user
def auth(username, password):
    """
    :param username:
    :param password:
    :return: boolean
    """

    # instantiates class
    auth_user_object = Database_Manager.UserTable()
    # returns true if login is correct
    auth_boolean = auth_user_object.get_user(str(username), str(password))
    # opens library if auth_boolean returns true  
    if auth_boolean == "True":
        open_library()
    else:
        # TODO: make warning box work
        messagebox.showwarning("Username and/or password incorrect."
                               "\nPlease Try Again")
        #


# TODO: make create user form
# def open_create_user():

# TODO: open delete user form
# def open_delete_user():

def open_library():
    master_library = Tk()
    main_library = PersonalLibrary(master_library)
    master_library.mainloop()


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
                                  command=lambda: [LoginPage(master).close(),
                                                   auth(self.Username, self.Password)])\
            .grid(column=0, row=7, pady=(10, 5))

        self.OptionLabel = Label(self.master, text="Or:").grid(column=0, row=8, padx=10, pady=20)

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


class PersonalLibrary:

    def __init__(self, master1):
        self.master1 = master1
        master1.title("My Library")  # names the form
        master1.geometry('600x360')  # width then height
        master1.resizable(0, 0)  # cannot resize form


# used to open the login page

root = Tk()  # runs form
login_page_object = LoginPage(root)  # instantiates the LoginPage
root.mainloop()  # keeps form running

#
# then open pdf
