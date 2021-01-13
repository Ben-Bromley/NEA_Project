import Database_Manager

username = input("Username: ")
password = input("Password: ")

test = Database_Manager.UserTable()
auth = test.get_user(username, password)
if auth:
    print("Access Granted")
