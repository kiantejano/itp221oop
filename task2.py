class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I'm studying {self.course}.")


student1 = Student("Reymart Tibe", 67, "BS Civil Engineering")
student2 = Student("John Rophi", 27, "BS Information Technology")
student3 = Student("Marvie Urmenita", 18, "BA Communication")


student1.introduce()
student2.introduce()
student3.introduce()