# Create a list of 10 student names and change the 3rd student's name.

students = []

for i in range(10):
    name = input(f"Enter student {i + 1} name: ")
    students.append(name)

print("Current list:", students)

new_name = input("Enter the new name for the 3rd student: ")
students[2] = new_name  # index 2 = 3rd student

print("Updated list:", students)
    