from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def login(self, user: str, credential: str) -> bool:
        pass

    @abstractmethod
    def logout(self, user: str) -> bool:
        pass


class PasswordAuth(Authentication):
    def __init__(self, store: dict):
        self.store = store

    def login(self, user: str, credential: str) -> bool:
        return self.store.get(user) == credential

    def logout(self, user: str) -> bool:
        return True


class OTPAuth(Authentication):
    def __init__(self, valid_otp: str):
        self.valid_otp = valid_otp

    def login(self, user: str, credential: str) -> bool:
        return credential == self.valid_otp

    def logout(self, user: str) -> bool:
        return True


if __name__ == "__main__":
    p = PasswordAuth({'alice': 'pass'})
    o = OTPAuth('1234')
    print(p.login('alice', 'pass'))
    print(o.login('bob', '1234'))
