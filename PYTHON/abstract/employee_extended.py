from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    @abstractmethod
    def display_details(self) -> str:
        pass


class Manager(Employee):
    def __init__(self, base: float, bonus: float):
        self.base = base
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base + self.bonus

    def display_details(self) -> str:
        return f"Manager: salary={self.calculate_salary():.2f}"


class Developer(Employee):
    def __init__(self, base: float, overtime: float):
        self.base = base
        self.overtime = overtime

    def calculate_salary(self) -> float:
        return self.base + self.overtime

    def display_details(self) -> str:
        return f"Developer: salary={self.calculate_salary():.2f}"


if __name__ == "__main__":
    m = Manager(5000, 1500)
    d = Developer(4000, 300)
    print(m.display_details())
    print(d.display_details())
