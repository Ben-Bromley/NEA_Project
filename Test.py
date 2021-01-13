import Database_Manager

print("\nWelcome to the sheet music manager \n" 
      "Please type A, B, or C for what you'd like to do: \n"
      "[A] Login to Your Account \n"
      "[B] Delete Your Account \n"
      "[C] Create a new account \n")
input("- ")
auth = "False"
while auth != "True":
    username = input("Username: ")
    password = input("Password: ")
    test = Database_Manager.UserTable()
    auth = test.get_user(username, password)

    if auth:
        break
    else:
        print("Access Denied")

print("Access Granted, Welcome", username)
