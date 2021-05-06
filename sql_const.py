# This file is here as a method of using sql statements as constants

# ALL USER TABLE SQL
# Initialising table
INIT_USER_TABLE = """CREATE TABLE IF NOT EXISTS Users (
                        USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USERNAME TEXT NOT NULL UNIQUE,
                        PASSWORD TEXT NOT NULL
                        )"""

GET_USER_ID = """SELECT USERID FROM users 
                WHERE USERNAME = ? AND PASSWORD = ?"""

# Delete user from table
DELETE_USER = """DELETE FROM Users
                WHERE USERNAME = ? AND PASSWORD = ?"""

# Add user to table
CREATE_USER = """INSERT INTO Users (
                    USERNAME, PASSWORD)
                    VALUES (?, ?) """

# Authenticate user to table
GET_USER = """SELECT USERID, USERNAME, PASSWORD FROM Users 
                WHERE USERNAME = ? AND PASSWORD = ?"""


# ALL LIBRARY TABLE SQL
# TODO: LEARN HOW TO BUILD RELATIONS
# TODO: Write remaining sql statements for this table
INIT_LIBRARY_TABLE = """CREATE TABLE IF NOT EXISTS Library (
                            LIBRARYID INTEGER PRIMARY KEY AUTOINCREMENT
                            USERID INTEGER FOREIGN KEY
                            PIECEID INTEGER NOT NULL)"""
# TODO: Make sure PIECEID is valid in table
# TODO: sort out primary key in library table
NEW_USER_LIBRARY = """INSERT INTO TABLE Library
                    (USERID,)"""

DELETE_USER_LIBRARY = """"""


# All MUSIC TABLE SQL
