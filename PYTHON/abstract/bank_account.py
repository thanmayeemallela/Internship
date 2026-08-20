from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, principal: float):
        self.principal = principal

    @abstractmethod
    def calculate_interest(self) -> float:
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self) -> float:
        rate = 0.04
        return self.principal * rate


class CurrentAccount(BankAccount):
    def calculate_interest(self) -> float:
        rate = 0.01
        return self.principal * rate


if __name__ == "__main__":
    s = SavingsAccount(1000)
    c = CurrentAccount(1000)
    print(f"Savings interest: {s.calculate_interest():.2f}")
    print(f"Current interest: {c.calculate_interest():.2f}")
