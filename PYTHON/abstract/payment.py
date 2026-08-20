from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class UPIPayment(Payment):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} via UPI ({self.upi_id})"


class CardPayment(Payment):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> str:
        masked = "****" + self.card_number[-4:]
        return f"Paid {amount:.2f} via Card ({masked})"


if __name__ == "__main__":
    upi = UPIPayment("user@upi")
    card = CardPayment("1234567812345678")
    print(upi.pay(250.0))
    print(card.pay(99.99))
