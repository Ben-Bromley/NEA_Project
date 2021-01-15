import Database_Manager

# Initialise UserTable object
test = Database_Manager.UserTable()


# authorises user and returns username
def auth_user():
    print("Login:")
    auth = "False"
    while auth != "True":
        username = input("Username: ")
        password = input("Password: ")

        auth = test.get_user(username, password)

        if auth:
            return username
            break
        else:
            print("Access Denied")


def create_user(): # TODO: Finish test login
    print("Enter a username:")
    new_username = input("~ ")


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

if welcome_option == 'A':
    # Gets username from user
    # authorises user
    user = auth_user()
    print("Access Granted, Welcome", user)

elif welcome_option == 'B':
    print("Please log in first:")
    auth_user()

elif welcome_option == 'C':
    print("Welcome to registration")
    create_user()