# Ben Bromley NEA project - 2020/21 - Wigston College

# for general tkinter
from tkinter import *
from tkinter import Tk, messagebox
from tkinter.ttk import *
# for file management
import os
from tkinter import filedialog
import shutil
# for database access
import databaseManager

# creates Tk as an instance of a tkinter form
login = Tk()

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


def auth_to_open(username, password):
    auth_boolean = auth(username, password)
    # opens library if auth_boolean returns true
    if auth_boolean:
        print("Auth returned True")
        login_page_object.close()
        open_library()
    else:
        # TODO: finish warning box work
        messagebox.showwarning("Username and/or password incorrect.")

# region init and open library


def open_library():
    library_form_object = init_library()
    library_form_object.open


def init_library():
    library = Tk()
    return PersonalLibrary(library)
# endregion
# region init and open create form


def open_create_form():
    create_form = init_create_form()
    create_form.open


def init_create_form():
    create = Tk()
    return CreateUserPage(create)
# endregion
# region init and open delete form


def open_delete_form():
    delete_form = init_delete_form()
    delete_form.open


def init_delete_form():
    delete = Tk()
    return DeleteUserPage(delete)
# endregion


class CreateUserPage:

    # creates the basic tkinter form
    def __init__(self, master):
        self.master = master
        self.master.title("Create Account")
        self.master.geometry('275x200')  # width then height
        self.master.resizable(0, 0)  # cannot resize form
        self.master['bg'] = 'light grey'

        # region username and password labels
        self.User_Lbl = Label(self.master, text="New Username:", anchor='w')\
            .grid(sticky='w', column=0, row=3, padx=(20, 0), pady=(10, 0))
        self.Pass_lbl = Label(self.master, text="New Password:", anchor='w')\
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

        # TODO: add another entry box for confirmation

        # region button & commands
        self.LoginButton = Button(self.master, text="Create Account",
                                  command=lambda: [self.createAccount(self.Username, self.Password)])\
            .grid(column=0, row=7, pady=(10, 5))
        # endregion

    def createAccount(self, Username, Password):
        new_username = Username.get()
        new_password = Password.get()
        databaseManager.userTable.create_user(new_username, new_password)

    def open(self):
        self.create_master.mainloop()

    def close(self):
        self.create_master.destroy()


class DeleteUserPage:

    # creates the basic tkinter form
    def __init__(self, master):
        self.master = master
        self.master.title("Delete Account")
        self.master.geometry('275x400')  # width then height
        self.master.resizable(0, 0)  # cannot resize form

        # intro label
        self.Top_Lbl = Label(self.master, text="Confirm details to delete account:") \
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
        self.LoginButton = Button(self.master, text="Delete",
                                  command=lambda: self.deleteAccount(self.Username, self.Password))\
            .grid(column=0, row=7, pady=(10, 5))

    def deleteAccount(self, Username, Password):
        if auth(Username, Password):
            pythonUsername = Username.get()
            pythonPassword = Password.get()
            databaseManager.userTable.delete_user(
                pythonUsername, pythonPassword)
            self.close()
        else:
            messagebox.showwarning("Invalid account details")

    def open(self):
        self.master.mainloop()

    def close(self):
        self.master.destroy()

# Login page


class LoginPage:
    #  sets up basic form properties
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome")  # names the form
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
                                   command=lambda: [LoginPage(master).close(), open_create_form()]) \
            .grid(column=0, row=9, pady=(5, 5))
        self.DeleteButton = Button(self.master, text="Delete your account",
                                   command=lambda: [LoginPage(master).close(), open_delete_form()])\
            .grid(column=0, row=10, pady=(5, 5))
        # endregion

    def open(self):
        self.master.mainloop()

    def close(self):
        self.master.destroy()


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
        self.DeleteButton = Button(self.library_master, text="Delete File",
                                   command=lambda: self.delete_file()).pack()
        # endregion

    def open():
        self.master.mainloop()

    def close():
        self.master.destroy()

    def import_file(self):
        # create directory
        try:
            os.mkdir('user-files/')
        # catches error if folder already exists
        except FileExistsError as exc:
            print(exc)
        # opens dialog box for user to select file
        file_to_import = filedialog.askopenfilename()
        print(f"user selected {file_to_import}")
        home_folder = 'user-files/'
        shutil.copy(file_to_import, home_folder)
        print("File imported successfully")
        return

    def export_file(self):
        # opens dialog box for user to select file
        file_to_export = filedialog.askopenfilename()
        print(f"user selected {file_to_export}")
        dst = "C://Users/Public/Documents/"
        shutil.copy(file_to_export, dst)
        print("File imported successfully")
        return

    def delete_file(self):
        file = filedialog.askopenfilename()
        # If the file exists, delete it
        if os.path.isfile(file):
            os.remove(file)
        else:
            print(f'Error: {file} not a valid filename')
        return


# used to open the login page
login_page_object = LoginPage(login)  # instantiates the LoginPage
login_page_object.open()  # keeps form running

# output after program closes
print("program finished")
