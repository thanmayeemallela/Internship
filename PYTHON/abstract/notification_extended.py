from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass

    @abstractmethod
    def schedule(self, recipient: str, message: str, when: datetime) -> str:
        pass


class Email(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"Email sent to {recipient}: {message}"

    def schedule(self, recipient: str, message: str, when: datetime) -> str:
        return f"Email scheduled to {recipient} at {when.isoformat()}"


class SMS(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"SMS sent to {recipient}: {message}"

    def schedule(self, recipient: str, message: str, when: datetime) -> str:
        return f"SMS scheduled to {recipient} at {when.isoformat()}"


class WhatsApp(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"WhatsApp sent to {recipient}: {message}"

    def schedule(self, recipient: str, message: str, when: datetime) -> str:
        return f"WhatsApp scheduled to {recipient} at {when.isoformat()}"


if __name__ == "__main__":
    when = datetime.now() + timedelta(hours=1)
    for cls in (Email(), SMS(), WhatsApp()):
        print(cls.send('user', 'Hello'))
        print(cls.schedule('user', 'Hello later', when))
