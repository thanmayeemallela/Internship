mobile = input("Enter mobile number: ")

if mobile.isdigit() and len(mobile) == 10:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")