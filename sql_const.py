# This file is here as a method of using sql statements as constants

# ALL USER TABLE SQL

# Initialising table
INIT_USER_TABLE = """CREATE TABLE IF NOT EXISTS Users (
                        USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USERNAME TEXT NOT NULL UNIQUE,
                        PASSWORD TEXT NOT NULL
                        )"""

# Delete user from table
DELETE_USER = """DELETE USERNAME, PASSWORD FROM Users
                WHERE USERNAME = ? AND PASSWORD = ?"""

# Add user to table
CREATE_USER = """INSERT INTO Users (
                    USERID, USERNAME, PASSWORD)
                    VALUES (?, ?, ?) """

# Authenticate user to table
AUTH_USER = """SELECT USERID, USERNAME, PASSWORD FROM Users 
                WHERE USERNAME = ? AND PASSWORD = ?"""


# ALL LIBRARY TABLE SQL
# TODO: LEARN HOW TO BUILD RELATIONS
# TODO: Write remaining sql statements for this table
INIT_LIBRARY_TABLE = """CREATE TABLE IF NOT EXISTS Library (
                            USERID INTEGER PRIMARY KEY
                            PIECEID INTEGER NOT NULL)"""

NEW_USER_LIBRARY = """SQL"""
# All MUSIC TABLE SQL


