# To access the system, the user must enter the username darth_vader and the password 1138.
# Create a script that receives and validates this login information.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username.lower() == "darth_vader" and password == "1138":
    print("Login successful!")
else:
    print("Unauthorized login!")