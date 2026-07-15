from student import Student


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def find_student(students, roll_no):
    for s in students:
        if s.roll_no == roll_no:
            return s
    return None


def add_student(students):
    print("\n--- Add Student ---")
    roll_no = get_int("Enter Roll Number: ")

    if find_student(students, roll_no) is not None:
        print("Roll Number already exists. Student not added.")
        return

    name = input("Enter Name: ").strip()
    while name == "":
        name = input("Name cannot be empty. Enter Name: ").strip()

    marks = get_int("Enter Marks (0-100): ")
    while not Student.validate_marks(marks):
        marks = get_int("Invalid marks. Enter Marks (0-100): ")

    students.append(Student(roll_no, name, marks))
    print("Student Added Successfully!")


def view_students(students):
    print("\n--- View All Students ---")
    if len(students) == 0:
        print("No students available.")
        return
    for s in students:
        s.show()


def search_student(students):
    print("\n--- Search Student ---")
    roll_no = get_int("Enter Roll Number to search: ")
    s = find_student(students, roll_no)

    if s is None:
        print("Student Not Found")
    else:
        s.show()


def update_marks(students):
    print("\n--- Update Marks ---")
    roll_no = get_int("Enter Roll Number to update: ")
    s = find_student(students, roll_no)

    if s is None:
        print("Student Not Found")
        return

    new_marks = get_int("Enter new Marks (0-100): ")
    while not Student.validate_marks(new_marks):
        new_marks = get_int("Invalid marks. Enter Marks (0-100): ")

    s.update_marks(new_marks)
    print("---- Marks Updated Successfully")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll_no = get_int("Enter Roll Number to delete: ")
    s = find_student(students, roll_no)

    if s is None:
        print("Student Not Found")
        return

    students.remove(s)
    print("Student Deleted Successfully")


def show_topper(students):
    print("\n--- Display Topper ---")
    if len(students) == 0:
        print("No students available.")
        return

    topper = students[0]
    for s in students[1:]:
        if s.marks > topper.marks:
            topper = s

    topper.show()


def menu():
    print("\n==============================")
    print("Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("\nEnter your choice: ").strip()
    return choice


def main():
    students = []

    while True:
        choice = menu()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_marks(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_topper(students)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
