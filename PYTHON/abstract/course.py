from abc import ABC, abstractmethod


class Course(ABC):
    @abstractmethod
    def start_course(self) -> str:
        pass

    @abstractmethod
    def get_duration(self) -> int:
        pass


class OnlineCourse(Course):
    def __init__(self, weeks: int):
        self.weeks = weeks

    def start_course(self) -> str:
        return "Online course started"

    def get_duration(self) -> int:
        return self.weeks


class OfflineCourse(Course):
    def __init__(self, days: int):
        self.days = days

    def start_course(self) -> str:
        return "Offline course started"

    def get_duration(self) -> int:
        return self.days


if __name__ == "__main__":
    o = OnlineCourse(6)
    f = OfflineCourse(10)
    print(o.start_course(), o.get_duration())
    print(f.start_course(), f.get_duration())
