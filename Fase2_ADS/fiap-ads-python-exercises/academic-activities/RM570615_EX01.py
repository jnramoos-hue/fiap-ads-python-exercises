# RM570615_EX01

# Initialize the vote counters for each weekday with zero
monday_votes = 0
tuesday_votes = 0
wednesday_votes = 0
thursday_votes = 0
friday_votes = 0

# Ask for the number of employees participating in the vote
employee_count = int(input("Enter how many employees will participate in the voting: "))

# Loop to collect each employee's vote
for v in range(employee_count):
    valid_vote = False

    # Use a while loop to make sure the user enters a valid weekday
    # If the input is invalid, the program asks again instead of skipping the vote
    while not valid_vote:
        vote = input(
            f"Employee {v + 1}, enter your preferred day (monday, tuesday, wednesday, thursday, friday): "
        ).lower()

        # Check the vote and update the corresponding counter
        if vote == "monday":
            monday_votes += 1
            valid_vote = True
        elif vote == "tuesday":
            tuesday_votes += 1
            valid_vote = True
        elif vote == "wednesday":
            wednesday_votes += 1
            valid_vote = True
        elif vote == "thursday":
            thursday_votes += 1
            valid_vote = True
        elif vote == "friday":
            friday_votes += 1
            valid_vote = True
        else:
            print("Invalid day! Please enter a weekday from Monday to Friday.")

# Find out which weekday received the highest number of votes
highest_vote = monday_votes
winning_day = "Monday"

if tuesday_votes > highest_vote:
    highest_vote = tuesday_votes
    winning_day = "Tuesday"

if wednesday_votes > highest_vote:
    highest_vote = wednesday_votes
    winning_day = "Wednesday"

if thursday_votes > highest_vote:
    highest_vote = thursday_votes
    winning_day = "Thursday"

if friday_votes > highest_vote:
    highest_vote = friday_votes
    winning_day = "Friday"

# Check if there is a tie
# Count how many times the highest vote total appears among the weekdays
ties = 0

if monday_votes == highest_vote:
    ties += 1
if tuesday_votes == highest_vote:
    ties += 1
if wednesday_votes == highest_vote:
    ties += 1
if thursday_votes == highest_vote:
    ties += 1
if friday_votes == highest_vote:
    ties += 1

# Output model
print("\n--- VOTING RESULT ---")
print(f"Monday: {monday_votes} vote(s).")
print(f"Tuesday: {tuesday_votes} vote(s).")
print(f"Wednesday: {wednesday_votes} vote(s).")
print(f"Thursday: {thursday_votes} vote(s).")
print(f"Friday: {friday_votes} vote(s).")
print("---------------------")

# If the highest vote total appears more than once, there is a tie
if ties > 1:
    print("RESULT: There was a TIE between the most voted days! A new vote will be required.")
else:
    print(f"RESULT: The chosen day for the live sessions was {winning_day} with {highest_vote} vote(s)!")