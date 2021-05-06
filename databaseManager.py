import sqlite3
import sql_const

# Class for managing the UserTab;e in the database


class UserTable(object):
    def __init__(self):
        # Connects to the database file
        self.db_connect = sqlite3.connect('music_database.db')
        # creates the cursor object
        self.c = self.db_connect.cursor()
        # see docstring of specified function
        self.create_table()

    def create_table(self):
        '''
        :return: Creates the user table if it doesn't already exist
        '''
        with self.db_connect:
            self.c.execute(sql_const.INIT_USER_TABLE)

    # Creates user
    def create_user(self, username, password):
        '''
        :param username:
        :param password:
        :return:
        '''
        with self.db_connect:
            self.c.execute(sql_const.CREATE_USER, (username, password))

    def delete_user(self, username, password):
        with self.db_connect:
            # Step 1: Get user ID (in order to delete user table)
            self.c.execute(sql_const.GET_USER_ID, (username, password))
            # test code to collect user id:
            user_id = self.c.fetchall()
            # Step 2: Deleting user
            self.c.execute(sql_const.DELETE_USER, (username, password))

            # TODO: Step 3: Remove Users Files
            # TODO: Step 4: Remove Library For User (delete where userid = ?)
            # self.c.execute(sql_const.DELETE_USER) - USER TABLE

    def get_user(self, username, password):
        # gets user details from database
        with self.db_connect:
            # selects uer record
            self.c.execute(sql_const.GET_USER, (username, password))
            # puts result into variable , returns "[]" if details incorrect
            user_details = self.c.fetchall()
            print(user_details)
            # if user_details has data, it prints the details
            if user_details:
                print(user_details)
                print("returning True")
                return True
            else:
                print("Returning False, Login Failed")
                return False

    def close_database(self):
        # closes database connection
        self.db_connect.close()


class LibraryTable(object):
    def __init__(self):
        self.db_connect = sqlite3.connect('music_database.db')
        self.c = self.db_connect.cursor()
        self.create_table()

    def create_table(self):
        with self.db_connect:
            self.c.execute(sql_const.INIT_LIBRARY_TABLE)

    def close_database(self):
        # closes database connection
        self.db_connect.close()
