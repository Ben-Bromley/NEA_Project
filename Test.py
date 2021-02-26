import databaseManager

# Initialise UserTable object
test = databaseManager.UserTable()


# authorises user and returns username
def auth_user():
    print("Login:")
    auth = "False"
    while auth != "True":
        username = input("Username: ")
        password = input("Password: ")

        auth = test.get_user(username, password)

        if auth:
            return username, True

        else:
            print("unauthorised.")


def create_user():  # TODO: Finish test login
    print("Enter a username:")
    new_username = input("~ ")
    print("Enter a password:")
    new_password = input("~ ")
    # sends new details to be added to .db
    test.create_user(new_username, new_password)
    print(f'welcome {new_username}')


# Main menu
print("\n Welcome to the sheet music manager \n"
      "Please type 1, 2, or 3 for what you'd like to do: \n"
      "[1] Login to Your Account \n"
      "[2] Delete Your Account \n"
      "[3] Create a new account \n")
# validate input!!
welcome_option = input("- ")

# Returning input
print(f'You chose: {welcome_option}')

if welcome_option == '1':
    # Gets username from user
    # authorises user
    user, authorised = auth_user()
    if authorised:
        print("Access Granted, Welcome", user)
    else:
        print("Accessed Denied")

elif welcome_option == '2':
    print("Please log in first:")
    auth_user()

elif welcome_option == '3':
    print("Welcome to registration")
    create_user()
