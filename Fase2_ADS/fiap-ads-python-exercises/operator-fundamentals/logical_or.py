# During its anniversary celebration, a store is offering discounts to customers:
# Purchases worth more than R$1000 will receive a 10% discount.
# Selected customers received the coupon FESTA, which also grants a 10% discount,
# regardless of the purchase amount.
# Discounts are not cumulative.
# Write a Python script that receives a coupon and the purchase amount from the user
# and displays the final purchase amount.

purchase_amount = float(input("Enter the purchase amount: "))
coupon = input("Enter the coupon name: ")

if purchase_amount >= 1000 or coupon == "FESTA":
    purchase_amount = purchase_amount * 0.9
else:
    print("Purchase without discount!")

print(f"Your purchase total is R${purchase_amount:.2f}")