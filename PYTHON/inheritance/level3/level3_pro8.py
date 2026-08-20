class BillingService:
    def create_bill(self, amount):
        print("Hospital bill:", amount)

class Hospital:
    def make_bill(self, billing):
        billing.create_bill(2500)

Hospital().make_bill(BillingService())
