combo_number = int(input("Enter the combo number: "))

match combo_number:
    case 1:
        dish_name = "Hamburger"
        dish_price = 12.50
    case 2:
        dish_name = "Cheeseburger"
        dish_price = 15.00
    case 3:
        dish_name = "Bacon Burger"
        dish_price = 17.00
    case _:
        dish_name = None
        dish_price = None

if dish_name:
    print(f"The selected meal is {dish_name}, and the combo price is R${dish_price}.")