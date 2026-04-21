# The team members were selected to receive a new-generation console as a reward.
# However, all five members must receive the same console.
# The program collects the vote of each team member and displays the selected console.

vote1 = input("Team member 1, enter which prize you want to receive: PLAYSTATION, XBOX or NINTENDO -> ")
vote2 = input("Team member 2, enter which prize you want to receive: PLAYSTATION, XBOX or NINTENDO -> ")
vote3 = input("Team member 3, enter which prize you want to receive: PLAYSTATION, XBOX or NINTENDO -> ")
vote4 = input("Team member 4, enter which prize you want to receive: PLAYSTATION, XBOX or NINTENDO -> ")
vote5 = input("Team member 5, enter which prize you want to receive: PLAYSTATION, XBOX or NINTENDO -> ")

playstation = 0
xbox = 0
nintendo = 0

if vote1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif vote1.upper() == "XBOX":
    xbox = xbox + 1
elif vote1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Team member 1 entered an invalid vote, so it will be ignored.")

if vote2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif vote2.upper() == "XBOX":
    xbox = xbox + 1
elif vote2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Team member 2 entered an invalid vote, so it will be ignored.")

if vote3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif vote3.upper() == "XBOX":
    xbox = xbox + 1
elif vote3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Team member 3 entered an invalid vote, so it will be ignored.")

if vote4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif vote4.upper() == "XBOX":
    xbox = xbox + 1
elif vote4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Team member 4 entered an invalid vote, so it will be ignored.")

if vote5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif vote5.upper() == "XBOX":
    xbox = xbox + 1
elif vote5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Team member 5 entered an invalid vote, so it will be ignored.")

if playstation > nintendo > xbox:
    print("The selected console was PlayStation.")
elif nintendo > playstation > xbox:
    print("The selected console was Nintendo.")
elif xbox > playstation > nintendo:
    print("The selected console was Xbox.")
else:
    print("There was a tie. Please contact management.")