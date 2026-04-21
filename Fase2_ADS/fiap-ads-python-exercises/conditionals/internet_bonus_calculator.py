# A telecommunications company is running a promotion where customers
# can receive internet browsing bonuses based on their score.
# 1000 points -> 3 GB bonus
# 500 points -> 1.5 GB bonus
# 200 points -> 500 MB bonus

# Ask the user for the customer's score
pontuacao = int(input("Please enter the customer's score: "))

# Check the score and display the corresponding bonus
if pontuacao >= 1000:
    print("You received a 3 GB bonus.")
elif pontuacao >= 500:
    print("You received a 1.5 GB bonus.")
elif pontuacao >= 200:
    print("You received a 500 MB bonus.")
else:
    print("You do not have enough points to redeem the bonus.")