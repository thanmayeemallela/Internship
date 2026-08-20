from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self, path: str) -> str:
        pass

    @abstractmethod
    def write(self, path: str, content: str) -> str:
        pass


class PDFFile(FileHandler):
    def read(self, path: str) -> str:
        return f"Reading PDF from {path} (simulated)"

    def write(self, path: str, content: str) -> str:
        return f"Writing PDF to {path} with content length {len(content)}"


class CSVFile(FileHandler):
    def read(self, path: str) -> str:
        return f"Reading CSV from {path} (simulated)"

    def write(self, path: str, content: str) -> str:
        return f"Writing CSV to {path} with rows {content.count('\n')+1}"


class ExcelFile(FileHandler):
    def read(self, path: str) -> str:
        return f"Reading Excel from {path} (simulated)"

    def write(self, path: str, content: str) -> str:
        return f"Writing Excel to {path} with sheets 1"


if __name__ == "__main__":
    handlers = [PDFFile(), CSVFile(), ExcelFile()]
    for h in handlers:
        print(h.read('file'))
        print(h.write('file', 'a,b,c\n1,2,3'))
