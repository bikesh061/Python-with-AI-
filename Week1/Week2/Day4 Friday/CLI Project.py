# Create an empty list to store all students
students = []


# Function to add a new student
def add_student():
    student = {}  # Create empty dictionary for one student
    student['id'] = input("Enter student ID: ")
    student['name'] = input("Enter student name: ")
    student['age'] = input("Enter student age: ")
    student['grade'] = input("Enter student grade: ")
    student['marks'] = input("Enter student marks: ")
    students.append(student)  # Add student dictionary to the list
    print("Student added successfully!\n")


# Function to display all students
def display_students():
    if not students:
        print("No students found.\n")
        return
    print("\nAll Students:")
    for student in students:
        print(
            f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}")
    print()


# Function to search a student by ID
def search_student():
    student_id = input("Enter student ID to search: ")
    for student in students:
        if student['id'] == student_id:
            print(
                f"Found Student: ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}\n")
            return
    print("Student not found!\n")


# Function to update student details
def update_student():
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            student['name'] = input(f"Enter new name (current: {student['name']}): ")
            student['age'] = input(f"Enter new age (current: {student['age']}): ")
            student['grade'] = input(f"Enter new grade (current: {student['grade']}): ")
            student['marks'] = input(f"Enter new marks (current: {student['marks']}): ")
            print("Student updated successfully!\n")
            return
    print("Student not found!\n")


# Function to delete a student
def delete_student():
    student_id = input("Enter student ID to delete: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")


# Main program loop
while True:
    print("=== Student Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-6.\n")
