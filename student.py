class Student:
    def __init__(self, name: str, roll_number: int, marks:float):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def add_student(self):
        file_name = "students.txt"
        with open (file_name, "a") as file:
            file.write(f"{self.name},{self.roll_number},{self.marks})\n")
        print("student added successfully")

    