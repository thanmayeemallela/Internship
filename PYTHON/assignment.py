#palindrome program.
text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
    # anagram program.
word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("Anagrams")
else:
    print("Not Anagrams")

#vowel-counting program.
text = input("Enter text: ").lower()

vowels = "aeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Vowel Count:", count)

# mobile-number validation program.
mobile = input("Enter mobile number: ")

if mobile.isdigit() and len(mobile) == 10:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

# password validation program.
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



