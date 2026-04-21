# Out-of-order values
values = [1, 7,19, 3, 2, 11, 15, 6, 1, 5, 2, 3]

# Displaying the list
print("The list was created like this: {}".format(values))

# Counting elements 1
counting = values.count(1)
print(f"The count of 1s was: {counting}")

# Reversing the list
values.reverse()
print(f"The reversed list looks like this: {values}")

# Ordering the list
values.sort(reverse=True)
print(f"The list in descending order looks like this: {values}")

# List Size
len(values)
quantities =  len(values)
print(f"The number of items is: {quantities}")

# Sum of elements
sum = sum(values)
print(f"The sum is: {sum}")