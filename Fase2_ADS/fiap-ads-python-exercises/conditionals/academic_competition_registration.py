# A university will hold an academic competition.
# Only adult students are automatically allowed to participate.

# Ask the student for the RM and age
rm = input("Please enter your student RM: ")
idade = int(input("Please enter your age: "))

# Check if the student is 18 or older
if idade >= 18:
    print(f"Your registration was completed successfully, student RM {rm}.")
    print("The details will be sent to your email!")
else:
    autorizacao = input("Do you have permission from your parents? Y - YES, N - NO: ")
    if autorizacao == "Y":
        print(f"Your participation was successfully authorized, student RM {rm}.")
        print("More information will be sent to your guardian's email.")
    else:
        print("Your participation was denied because you are not an adult.")

print("The program will now be closed.")