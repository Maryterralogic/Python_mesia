import random
def generate_employee_details(num_employees):
    cities = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]

    for _ in range(num_employees):
        emp_id = random.randint(1, 9999)
        emp_location = random.choice(cities)
        emp_salary = random.randint(20000, 150000)
        yield {"Emp Id": emp_id, "Emp Location": emp_location, "Emp Salary": emp_salary}

# Get the number of employee details to generate from the command line
num_employees_to_generate = int(input("Enter the number of employee details to generate: "))

# Generate employee details using the generator function
employee_generator = generate_employee_details(num_employees_to_generate)

# Using the generator to display employee details
for _ in range(num_employees_to_generate):
    employee = next(employee_generator)
    print("Employee Details:")
    print("Emp Id:", employee["Emp Id"])
    print("Emp Location:", employee["Emp Location"])
    print("Emp Salary:", employee["Emp Salary"])
    print()
