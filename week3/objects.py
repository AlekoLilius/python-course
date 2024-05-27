class Human:
    # Static variable
    num_of_humans = 0

    # Initilizing function (constructor)
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Human.num_of_humans += 1

    # String representation when calling Human object
    def __str__(self) -> str:
        return f"This is an object of the class Human: {self.name}, {self.age}"
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

class Student(Human):
    def __init__(self, name, age, grade, class_school) -> None:
        # super function from parent class Human
        super().__init__(name, age)
        self.grade = grade
        self.class_school = class_school

    def study(self):
        print(f"{self.name} is in {self.class_school}")
    
    def _grade_(self):
        return self.grade
    
    def get_grade(self):
        print(f"Student grade: {self.grade}")

human1 = Human('Adam', 18)
human2 = Human('Eve', 18)

human1.say_hello()
print(Human.num_of_humans)
print(human1.num_of_humans)
print(human1)
print(human2)

student1 = Student('John', 21, 'A', "First Class")
student1.say_hello()
student1.study()
print(student1._grade_()) # should not work
student1.get_grade()