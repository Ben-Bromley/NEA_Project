import sqlite3
import sql_const


class UserTable(object):
    def __init__(self):
        self.db_connect = sqlite3.connect('music_database.db')
        self.c = self.db_connect.cursor()
        self.create_database()

    def create_database(self):
        with self.db_connect:
            self.c.execute(sql_const.INIT_USER_TABLE)

    # Create user
    def create_user(self, user_id, username, password):
        with self.db_connect:
            self.c.execute(sql_const.CREATE_USER, (user_id, username, password))

    def delete_user(self, user_id, username, password, library_id):
        with self.db_connect:
            self.c.execute()

    def auth_user(self, username, password):
        with self.db_connect:
            self.c.execute()

    def close_database(self):
        # closes database connection
        self.db_connect.close()



'''
table = UserTable()
table.create_database()
'''

