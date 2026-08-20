from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass

    @abstractmethod
    def export(self, path: str) -> str:
        pass


class PDFReport(Report):
    def __init__(self):
        self.content = ""

    def generate(self, data: dict) -> str:
        self.content = f"PDF report with {len(data)} items"
        return self.content

    def export(self, path: str) -> str:
        return f"Exported PDF to {path}"


class ExcelReport(Report):
    def __init__(self):
        self.content = ""

    def generate(self, data: dict) -> str:
        self.content = f"Excel report with {len(data)} rows"
        return self.content

    def export(self, path: str) -> str:
        return f"Exported Excel to {path}"


if __name__ == "__main__":
    pdf = PDFReport()
    ex = ExcelReport()
    print(pdf.generate({'a': 1, 'b': 2}))
    print(pdf.export('out.pdf'))
    print(ex.generate({'r1': 1}))
    print(ex.export('out.xlsx'))
