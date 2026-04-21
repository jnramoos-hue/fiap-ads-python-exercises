# Request purchase information from the customer
value_buy = input("Enter the purchase amount: ")
cupom = input("Enter the discount coupon: ")

# Perform the conditional check
if cupom.upper() == "NIVER10":
    # Calculate a 10% discount
    value_bill = float(value_buy) * 0.9
else:
    value_bill = float(value_buy)
    print("INVALID COUPON")

# Display the final purchase amount
print(f"The final purchase amount is {value_bill:.2f}")
