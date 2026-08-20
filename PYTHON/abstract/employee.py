from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass


class Developer(Employee):
    def work(self) -> str:
        return "Writing code"


class Tester(Employee):
    def work(self) -> str:
        return "Testing software"


if __name__ == "__main__":
    dev = Developer()
    tester = Tester()
    print(dev.work())
    print(tester.work())
