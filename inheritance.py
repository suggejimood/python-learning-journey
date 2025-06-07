class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(f"First Name: {self.firstName} \nLast Name: {self.lastName}")

p1 = Person("Mehmet", "TAN")
p1.printName()

class Student(Person):
    pass
s1 = Student("Michèle", "Mouton")
s1.printName()