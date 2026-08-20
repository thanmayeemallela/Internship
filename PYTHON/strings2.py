#Level 1: Basic Strings
#Create a string containing your name and print it.
#Create a string containing your college name and print its length.
#Create a string and print its first character.
#Create a string and print its last character.
#Create a string and print the first 5 characters using slicing.
#Create a string and print the last 5 characters using slicing.
#Create a string and print the string in reverse order.
#Create two strings and concatenate them.
#Create a string and check whether a particular character exists in it.
#Create a string and check whether a particular word exists in it.

name="THANMAYEE"
print(name)

college="aditya"
print(len(college))

str="SWAPNA"
print(str[0])

str="SWAPNA"
print(str[-1])

str="swapna"
print(str[0:5])
print(str[-5:])

str="natya"
print(str[ : :-1])

s1="tirupathi"
s2="reddy"
s3=s1+s2
print(s3)

str="thanmayee"
print('a' in str)
print('s' in "swapna")

str="swapna malle"
print("swapna" in str)