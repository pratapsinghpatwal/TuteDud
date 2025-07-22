# Step 1: Create a dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Eva": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 and 4: Retrieve and display marks or show 'not found' message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
