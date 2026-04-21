# RM570615_EX04.py

# Validate the investment type
investment_type = int(input("""
Choose the investment type
 1. CDB
 2. LCI
 3. LCA
Enter the investment type (1, 2 or 3): """))

while investment_type < 1 or investment_type > 3:
    print("\n----Invalid type!----")
    investment_type = int(input("""
Choose the investment type
 1. CDB
 2. LCI
 3. LCA
Enter the investment type (1, 2 or 3): """))

gross_amount = float(input("Enter the amount to be redeemed: R$ "))
days = int(input("Enter the number of days the amount remained invested: "))

# Tax rate
if investment_type == 1:
    investment_name = "CDB"
    if days <= 180:
        tax_rate = 22.5
    elif days <= 360:
        tax_rate = 20.0
    elif days <= 720:
        tax_rate = 17.5
    else:
        tax_rate = 15.0
elif investment_type == 2:
    investment_name = "LCI"
    tax_rate = 0
else:
    investment_name = "LCA"
    tax_rate = 0

tax_amount = gross_amount * (tax_rate / 100)
net_amount = gross_amount - tax_amount

# Direct and organized output
print("\n--- REDEMPTION SUMMARY ---")
print(f"Investment: {investment_name}")
print(f"Gross Amount: R$ {gross_amount:.2f}")
print(f"Days: {days}")
print(f"Tax Rate: {tax_rate}%")
print(f"Income Tax: R$ {tax_amount:.2f}")
print(f"Net Amount: R$ {net_amount:.2f}")
