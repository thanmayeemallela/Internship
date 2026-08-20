from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

    @abstractmethod
    def refund(self, amount: float) -> str:
        pass


class UPI(Payment):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} via UPI {self.upi_id}"

    def refund(self, amount: float) -> str:
        return f"Refunded {amount:.2f} to UPI {self.upi_id}"


class CreditCard(Payment):
    def __init__(self, card_no: str):
        self.card_no = card_no

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} via Card ****{self.card_no[-4:]}"

    def refund(self, amount: float) -> str:
        return f"Refunded {amount:.2f} to Card ****{self.card_no[-4:]}"


class NetBanking(Payment):
    def __init__(self, account: str):
        self.account = account

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} via NetBanking ({self.account})"

    def refund(self, amount: float) -> str:
        return f"Refunded {amount:.2f} to NetBanking ({self.account})"


if __name__ == "__main__":
    methods = [UPI('user@upi'), CreditCard('1234567890123456'), NetBanking('AC123')]
    for m in methods:
        print(m.pay(100.0))
        print(m.refund(10.0))
