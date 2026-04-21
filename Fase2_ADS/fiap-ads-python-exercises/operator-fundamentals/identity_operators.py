# Assign string values to variables
city_1 = "São Paulo"
city_2 = "São Paulo"
city_3 = "Rio de Janeiro"

# Display the memory address of each variable
print(id(city_1))
print(id(city_2))
print(id(city_3))

# Identity operator comparisons
print(city_1 is city_2)
print(city_1 is not city_3)
print(city_1 is city_3)
