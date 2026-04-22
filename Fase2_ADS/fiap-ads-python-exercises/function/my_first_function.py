# Function that calculates the average speed
def calculateAverageSpeed():
    # Request distance and time
    distance = float(input("Enter the distance traveled: "))
    time = float(input("Enter the travel time: "))

    # Calculate average speed
    average_speed = distance / time

    #Display the result
    print("The average speed is {} km/h".format(average_speed))

#Here begins the main program
calculateAverageSpeed()



