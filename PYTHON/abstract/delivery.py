from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self, distance_km: float, weight_kg: float) -> float:
        pass

    @abstractmethod
    def deliver(self, address: str) -> str:
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self, distance_km: float, weight_kg: float) -> float:
        return 5 + 0.5 * distance_km + 0.2 * weight_kg

    def deliver(self, address: str) -> str:
        return f"Standard delivery to {address} scheduled"


class ExpressDelivery(Delivery):
    def calculate_charge(self, distance_km: float, weight_kg: float) -> float:
        return 10 + 1.0 * distance_km + 0.5 * weight_kg

    def deliver(self, address: str) -> str:
        return f"Express delivery to {address} scheduled"


if __name__ == "__main__":
    s = StandardDelivery()
    e = ExpressDelivery()
    print(s.calculate_charge(10, 2))
    print(e.calculate_charge(10, 2))
