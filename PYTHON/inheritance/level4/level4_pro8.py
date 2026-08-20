class Person:
    def introduce(self):
        print("This is a person")

class Teacher(Person):
    pass

print("Teacher IS-A Person")
Teacher().introduce()
