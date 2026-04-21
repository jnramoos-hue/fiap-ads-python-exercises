# RM570615_EX03.py

debt = float(input("Enter the debt amount: "))

# Direct header
print("\nDebt \t\t Interest \t\t Installments \t Installment Amount")

# Case for 1 installment
print(f"R$ {debt:.2f} \t R$ 0.00 \t 1 \t\t R$ {debt:.2f} \t R$ {debt:.2f}")

# Loop for installments: 3, 6, 9, 12
interest_rate = 10

for installment_quantity in range(3, 13, 3):
    interest_amount = debt * (interest_rate / 100)
    total_amount = debt + interest_amount
    installment_amount = total_amount / installment_quantity

    # Formatted output with one or two \t for basic alignment
    print(f"R$ {total_amount:.2f} \t R$ {interest_amount:.2f} \t {installment_quantity} \t\t R$ {installment_amount:.2f}")

    # Increase the interest by 5% for the next line
    interest_rate += 5