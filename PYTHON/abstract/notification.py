from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass


class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"Email sent to {recipient}: {message}"


class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"SMS sent to {recipient}: {message}"


if __name__ == "__main__":
    e = EmailNotification()
    s = SMSNotification()
    print(e.send("alice@example.com", "Hello Alice"))
    print(s.send("+1234567890", "Hello Bob"))
