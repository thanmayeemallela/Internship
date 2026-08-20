class ReportGenerator:
    def create_report(self, name):
        print("Report created for", name)

class Employee:
    def make_report(self, generator):
        generator.create_report("Rupa")

Employee().make_report(ReportGenerator())
