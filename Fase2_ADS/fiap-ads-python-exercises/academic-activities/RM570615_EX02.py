# RM570615_EX02

# Receive the car price
car_price = float(input("Enter the car price: "))

# Calculate the cash price with a 20% discount
# This value will be the base for all the other calculations in the table
cash_price = car_price * 0.80

# Display the first part of the output
print(f"Final cash price with a 20% discount: R$ {cash_price:.2f}")

# Loop using range for the installment options (from 6 to 60, increasing by 6)
# Interest starts at 3% for 6 installments and increases by 3% each time
interest_rate = 3

for installments in range(6, 61, 6):
    # The additional amount is calculated based on the cash price
    additional_amount = cash_price * (interest_rate / 100)
    final_price = cash_price - additional_amount

    # Calculate the value of each installment
    installment_value = final_price / installments

    # Display the formatted data
    # Use \t to create table-like spacing
    print(f"R$ {final_price:.2f} \t {installments} \t {installment_value:.2f}")

    # Increase the interest rate by 3% for the next line in the table
    interest_rate += 3