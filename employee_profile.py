# Employee Profile Generator

# Personal Information
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'

# Employee Details
employee_age = 28
position = 'Data Analyst'
salary = 75000
years_experience = 5

# Employee Code
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]

# Display Information
print("=" * 50)
print("EMPLOYEE PROFILE")
print("=" * 50)

# Employee Card
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Experience
experience_info = f'Experience: {years_experience} years'
print(experience_info)

# Address
print(f'Address: {address}')

# Code Information
print(f'\nEmployee Code: {employee_code}')
print(f'Department: {department}')
print(f'Year: {year_code}')
print(f'Initials: {initials}')
print("=" * 50)
