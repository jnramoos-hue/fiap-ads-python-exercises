categories = ("A", "B", "C", "D", "E" )



categories = input("Enter your deiver's license category: ")

if categories in categories:
    print("Existing category!")
else:
    print("Non-existing category!")


