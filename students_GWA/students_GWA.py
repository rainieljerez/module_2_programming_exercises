#Jerez, Joaqui Rainiel A.
#BSCpE 1-4
#represents the record of the students
class Student:

    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

    def __str__(self):
        return f"{self.name} - GWA: {self.gwa: .2f}"
#reads file, finds the student with highest gwa, and print
class StudentHighestGWA:

    def __init__(self, filename):
        self.filename = filename
        self.students = []
#reads the file
    def read_students(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        name = parts[0].strip()
                        gwa = parts [1].strip()
                        student = Student(name, gwa)
                        self.students.append(student)
            print (f"Successfully loaded {len(self.students)} students.\n")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
#looks for student with the highest gwa
    def find_highest_gwa(self):

        if not self.students:
            print("No student records found.")
            return None

        top_student = min(self.students, key=lambda s: s.gwa)
        return top_student
#prints the student name and gwa
    def display_top_student(self):

        top = self.find_highest_gwa()
        if top:
            print("\n STUDENT WITH HIGHEST GWA:")
            print("=" * 35)
            print(f"   Name : {top.name}")
            print(f"   GWA  : {top.gwa:.2f}")
            print("=" * 35)

def main():
        records = StudentHighestGWA("students.txt")
        records.read_students()
        records.display_top_student()

if __name__ == "__main__":
    main()
