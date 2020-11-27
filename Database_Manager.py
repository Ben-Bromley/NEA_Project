import sqlite3


class UserTable(object):
    def __init__(self):
        self.db_connect = sqlite3.connect('music_database.db')
        self.c = self.db_connect.cursor()
        self.create_database()

    def create_database(self):
        with self.db_connect:
            self.c.execute("""CREATE TABLE IF NOT EXISTS Users (
                        USERID INTEGER PRIMARY KEY,
                        USERNAME TEXT NOT NULL,
                        PASSWORD TEXT NOT NULL
                            )""")

    def create_user(self, user_id, username, password):
        with self.db_connect:
            self.c.execute('''INSERT INTO TABLE Users
             ()''')

    def close_database(self):
        # closes database connection
        self.db_connect.close()



'''
table = UserTable()
table.create_database()
'''

