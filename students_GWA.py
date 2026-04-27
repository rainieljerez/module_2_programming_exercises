

#represents the record of the students
class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

    def __str__(self):
        return f"{self.name} - GWA: {self.gwa: .2f}"
    
