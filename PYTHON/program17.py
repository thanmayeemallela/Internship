email = input("Enter email address: ")

if "@" in email and "." in email:
    print("Basic Email Format is Valid")
else:
    print("Invalid Email Format")