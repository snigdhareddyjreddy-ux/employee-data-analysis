import pandas as pd

# Load employee data
df = pd.read_csv("employee_data.csv")

print("===== Employee Data =====")
print(df)

# Calculate average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count employees in each department
department_count = df["Department"].value_counts()
print("\nDepartment Count:")
print(department_count)

# Ask user for salary threshold
threshold = int(input("\nEnter salary threshold: "))

# Filter employees
filtered = df[df["Salary"] > threshold]

print("\nEmployees with salary greater than", threshold)
print(filtered)

# Save filtered employees
filtered.to_csv("filtered_employees.csv", index=False)

print("\nFiltered data saved as 'filtered_employees.csv'")
