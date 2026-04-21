# Initialize the menu option
opcao = 0

# Keep the system running until the user chooses option 4
while opcao != 4:
    print("1 - Run feature 1")
    print("2 - Run feature 2")
    print("3 - Run feature 3")
    print("4 - Exit the system")

    # Check which option was selected
    if opcao == 1:
        print("Running feature 1")
    elif opcao == 2:
        print("Running feature 2")
    elif opcao == 3:
        print("Running feature 3")
    elif opcao == 4:
        print("Exiting the system...")
    else:
        print("Invalid option.")

