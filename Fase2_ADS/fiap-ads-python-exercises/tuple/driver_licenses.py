# Method to validate th informed category
def validate_category (user_category):
    # Checking if the category typed by the user is present in the list
    if user_category.upper() in categories:
        # if it is, this message is displayed
        print("Valid category!")
    else:
        # If it is not, this message is displayed
        print("Invalid category!")

# List with DVLA driver's license categories
categories = ["A", "B", "C", "D", "E"]



