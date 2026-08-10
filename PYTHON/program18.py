password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password")
else:
    print("Weak Password")