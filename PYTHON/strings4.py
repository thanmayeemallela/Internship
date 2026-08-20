#Level 3: String Validation
#Create a string containing only numbers and check it using isdigit().
#Create a string containing alphabets and numbers and check it using isalnum().
#Create a string containing spaces and check it using isspace().
#Create a string and check whether it contains lowercase letters using islower().
#Create a string and check whether it contains uppercase letters using isupper().
#Create a string and check whether it is in title case using istitle().
#Ask the user to enter a username and check whether it contains only alphabets and numbers.
#Ask the user to enter a password and check whether it contains at least one digit.
#Ask the user to enter a string and check whether it is empty or contains characters.
#Ask the user to enter an email address and check whether it contains "@" and ".".

str="2008"
print(str.isdigit())

str="thanmayee2008"
print(str.isdigit())

str = "thanu2008"
print(str.isalnum())

str = " "
print(str.isspace())

str = "hello"
print(str.islower())

str = "HELLO"
print(str.isupper())

str = "Hello World"
print(str.istitle())

uname = input("Enter username: ")
if uname.isalnum():
    print("Valid username")
else:
    print("Invalid username")


str = input("Enter a string: ")
if str == "":
    print("String empty")
else:
    print("String contains characters")    


email = input("Enter email address: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email") 


password=input("enter password")
for ch in password:
 if ch.isdigit():
    print("conatins digit")
    break
 else :
    print("doesn't contain digit")