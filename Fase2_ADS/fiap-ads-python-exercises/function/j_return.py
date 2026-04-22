def average_speed(distance, time):
    avg_speed = distance / time
    return avg_speed

averages_speed = []
for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    dist = float(input(f"Enter the distance traveled on {day} "))
    time = float(input(f"Ente the travel time on {day} "))
    averages_speed.append(average_speed(dist, time))

print(f"The average speed of week was {averages_speed}")
