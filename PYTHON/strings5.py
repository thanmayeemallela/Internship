#Level 4: Strings with Loops
#Write a program to count the number of vowels in a string.
#Write a program to count the number of consonants in a string.
#Write a program to count the number of digits in a string.
#Write a program to count the number of spaces in a string.
#Write a program to count uppercase and lowercase characters separately.
#Write a program to print each character of a string on a separate line.
#Write a program to print only the vowels from a string.
#Write a program to print only the consonants from a string.
#Write a program to remove all spaces from a string without using replace().
#Write a program to reverse a string without using slicing or reversed().

str="thanmayee"
str2=str.lower()
count=0
for ch in str:
    if ch in "aeiou":
      count=count+1
print("vowels:",count)


str="thanmayee"
str2=str.lower()
count=0
for ch in str:
    if ch  not in "aeiou":
      count=count+1
print("consonants",count)


str="thanu@2008"
count=0
for ch in str:
    if ch.isdigit():
       count=count+1
print("digits: ",count)       
     

str="thanmayee mallela"
count=0
for ch in str:
    if ch.isspace():
       count=count+1
print("spaces: ",count)  


str="Thanmayee Mallela"
count1=0
count2=0
for ch in str:
    if ch.isupper():
       count1=count1+1
    if ch.islower(): 
       count2=count2+1
print("uppercase:",count1)
print("lowercase:",count2)  


str="swapna"
for ch in str:
    print(ch)


str="swapna"
str2=str.lower()
count=0
for ch in str:
    if ch in "aeiou":
       print(ch,end="")  


str="thanmayee"
str2=str.lower()
count=0
print("\n")
for ch in str:
    if ch  not in "aeiou":
       print(ch,end="") 


print("\n")
str1=" thanmayee mallela "
str=""
for ch in str1:
    if ch!=" ":
         str+=ch
print(str)    


print("\n")
str="thanu"
str1=""
for ch in str:
     str1=ch+str1
      
print(str1)