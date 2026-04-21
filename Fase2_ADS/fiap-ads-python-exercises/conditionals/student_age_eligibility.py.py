# A university will hold an academic competition.
# Only adult students are allowed to participate.

# Ask the student for the RM and age
rm = input("Please enter your student RM: ")
idade = int(input("Please enter your age: "))

# Check if the student is 18 or older
if idade >= 18:
    print(f"Your registration was completed successfully, student RM {rm}.")
    print("The details will be sent to your email.")
else:
    print("Your participation was denied because you are not an adult.")

print("The program will now be closed.")