employees = {}

while input("Do you want to add an employee? Y-Yes, N-No").upper() != "N":
    name = input("Enter the employee's name: ")
    role = input("Enter the employee's role: ")
    #employees.update({name: role})
    employees[name] = role

print(employees)
