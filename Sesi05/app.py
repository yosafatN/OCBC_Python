class Dog:
    species = "Bulldog"

    def __init__(self, name, age):
        self.name = name
        self.umur = age

    def toString(self):
        print(self.name, self.umur)

    def withParameter(self, parameter):
        print(self.name, self.umur, parameter)


dog = Dog("Doggy", "2")

print(dog.species)
dog.toString()
dog.withParameter("Parameter")
print(dog.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def printStudent(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"


yosafat = Student("Yosafat", 22, 100)
print(yosafat.printStudent())
print(yosafat.name)
