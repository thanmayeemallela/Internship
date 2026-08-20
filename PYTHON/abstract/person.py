from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def role(self) -> str:
        pass


class Student(Person):
    def role(self) -> str:
        return "Learner"


class Teacher(Person):
    def role(self) -> str:
        return "Instructor"


if __name__ == "__main__":
    print(Student().role())
    print(Teacher().role())
