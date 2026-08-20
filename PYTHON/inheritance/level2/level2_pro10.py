class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Latha"), Doctor("Sri")]
        self.patients = [Patient("Rupa"), Patient("Mahi")]

    def show_details(self):
        print("Doctors:")
        for doctor in self.doctors:
            print(doctor.name)
        print("Patients:")
        for patient in self.patients:
            print(patient.name)

Hospital().show_details()
