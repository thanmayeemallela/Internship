#Level 2: String Methods
#Create a string and convert it to uppercase using upper().
#Create a string and convert it to lowercase using lower().
#Create a string and convert the first character to uppercase using capitalize().
#Create a sentence and convert the first letter of every word to uppercase using title().
#Create a string and swap uppercase characters to lowercase and lowercase characters to uppercase using swapcase().
#Create a string containing extra spaces and remove the spaces using strip().
#Create a string with spaces at the beginning and remove them using lstrip().
#Create a string with spaces at the end and remove them using rstrip().
#Create a string and replace one word with another using replace().
#Create a string and count how many times a particular character appears using count().
#Create a string and find the position of a particular character using find().
#Create a string and find the position of a particular word using index().
#Create a string and check whether it starts with a particular word using startswith().
#Create a string and check whether it ends with a particular word using endswith().
#Create a string containing only alphabets and check it using isalpha().

str="thanmayee"
print(str.upper())

str="THANU"
print(str.lower())

str="     BHAVYA"
str1="**BHAVYA"
print(str.strip())
print(str1.strip("*"))

str="thanmayee"
print(str.capitalize())

str="thanmayee mallela"
print(str.title())

str="   rupa"
print(str.lstrip())

str="rupa   "
print(str.rstrip())

str="thanmayee mallela"
print(str.replace("rupa","sri"))

str="thanmayee"
print(str.count('a'))

str="thanmayee"
print(str.find('l'))

str="hello lakshmi"
print(str.index("lakshmi"))

str="thanmayee mallela"
print(str.startswith('t'))
print(str.startswith('m'))
print(str.startswith("thanmayee"))

str="thanmayee mallela "
print(str.endswith('a'))
print(str.endswith("mallela"))

str="rupa@"
str2="rupa"
print(str.isalpha())
print(str2.isalpha())



