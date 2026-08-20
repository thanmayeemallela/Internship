class CertificateGenerator:
    def generate(self, student):
        print("Certificate generated for", student)

class Course:
    def complete(self, certificate):
        certificate.generate("Rupa")

Course().complete(CertificateGenerator())
