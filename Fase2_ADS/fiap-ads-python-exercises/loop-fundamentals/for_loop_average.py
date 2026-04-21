# Variable to store the total weight of the boxes
total_weight = 0.0

# Loop that repeats 100 times to request the weight of each box
for i in range(1, 101):
    # For each loop iteration, request the weight of the box
    current_weight = float(input("Enter the weight of the box: "))

    # Add each entered weight to the total weight
    total_weight = total_weight + current_weight

# After the loop ends, calculate the arithmetic average
average = total_weight / 100

# Display the results
print(f"The total weight of the boxes is: {total_weight:.2f}.\nThe average weight is: {average:.2f}.")