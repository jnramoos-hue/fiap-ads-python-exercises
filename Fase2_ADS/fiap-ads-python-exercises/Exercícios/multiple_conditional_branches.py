# A travel agency is offering progressive discounts on travel packages
# based on the number of travelers living in the same household.
# The program must receive the gross package price, the seat category,
# and the number of travelers, then calculate the discount according to the rules.

# ---------------------------|
# Economy                    |
# 2 travelers: 3%            |
# 3 travelers: 4%            |
# 4 travelers or more: 5%    |
# ---------------------------|

# ---------------------------|
# Business                   |
# 2 travelers: 5%            |
# 3 travelers: 7%            |
# 4 travelers or more: 8%    |
# ---------------------------|

# ---------------------------|
# First Class                |
# 2 travelers: 10%           |
# 3 travelers: 15%           |
# 4 travelers or more: 20%   |
# ---------------------------|

gross_price = float(input("Enter the ticket price: "))
category = input("Enter the seat category: ECONOMY, BUSINESS or FIRST CLASS: ")
number_of_travelers = int(input("Enter the number of travelers: "))
discount_value = 0

if category.upper() == "ECONOMY":
    if number_of_travelers == 2:
        discount_value = gross_price * 0.03
    elif number_of_travelers == 3:
        discount_value = gross_price * 0.04
    elif number_of_travelers >= 4:
        discount_value = gross_price * 0.05

elif category.upper() == "BUSINESS":
    if number_of_travelers == 2:
        discount_value = gross_price * 0.05
    elif number_of_travelers == 3:
        discount_value = gross_price * 0.07
    elif number_of_travelers >= 4:
        discount_value = gross_price * 0.08

elif category.upper() == "FIRST CLASS":
    if number_of_travelers == 2:
        discount_value = gross_price * 0.10
    elif number_of_travelers == 3:
        discount_value = gross_price * 0.15
    elif number_of_travelers >= 4:
        discount_value = gross_price * 0.20

else:
    print("Discount does not apply.")

net_price = gross_price - discount_value
average_per_traveler = net_price / number_of_travelers

print("""
---------------------------------------------------------------------------------
-> The total trip price is R${}.                                       

-> After the discount of R${}, the trip will cost R${}.  

-> The average cost per traveler is R${}.                         
---------------------------------------------------------------------------------

""".format(gross_price, discount_value, net_price, average_per_traveler))