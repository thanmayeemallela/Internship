n=int(input("enter a number to check: "))
temp=n
pal=0
while n>0:
    rev=n%10
    pal=pal*10+rev
    n=n//10
if temp==pal:
    print("it is a palindrome no")
else:
    print("it is not a palindrome no")    