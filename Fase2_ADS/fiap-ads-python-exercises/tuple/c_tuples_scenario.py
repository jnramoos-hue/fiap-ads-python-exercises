enemies = [(10, 5), (30,3), (1,50)]

while len(enemies) > 0:
    x = int(input("Enter a value for the X axis: "))
    y = int(input("Enter a value for the Y axis: "))

    if (x, y) in enemies:
        print("You hit an enemy!")
        enemies.remove((x, y))
    else:
        print("You missed!")

    print(f"now there are {len(enemies)} enemies left on the map.")
