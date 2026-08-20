from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass


class MySQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to MySQL database"


class PostgreSQLDatabase(Database):
    def connect(self) -> str:
        return "Connected to PostgreSQL database"


if __name__ == "__main__":
    print(MySQLDatabase().connect())
    print(PostgreSQLDatabase().connect())
