# Creating an empty list
jedi = []
print(type(jedi))

# Creating a list with the Jedi, Yoda, Luke, Obi-Wan, Anakin
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# Displaying a complete list
print(jedi)

# Displaying a specific position in the list
print(jedi[1])

# Displaying the last elements
print(jedi[-1])
print(jedi[1:3])

# Displaying each item in the list.
for name in jedi:
    print(name)