jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

print(f'The original list contains: \n{jedi}')

#Insertion at the end of the list
jedi.append("Luminara")
print(f'After insertion, the list contains: \n{jedi}')

#Insertion at the end of the list with input
jedi.append(input("Insert the name of a Jedi: "))
print(f'After insertion, the list contains: \n{jedi}')

#Insertion at a specific position
jedi.insert(1, "Charles")
print(f'After insertion at the indicated position, the list contains: \n{jedi}')