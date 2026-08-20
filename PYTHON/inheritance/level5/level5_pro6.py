class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

class BillingService:
    def bill(self):
        print("Bill created")

class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Latha")]
        self.patients = [Patient("Rupa")]

    def create_bill(self, billing):
        billing.bill()

hospital = Hospital()
print("Hospital HAS-A Doctors and Patients")
print("Hospital USES-A BillingService")
hospital.create_bill(BillingService())
