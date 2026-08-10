text = input("Enter text: ").lower()

vowels = "aeiou"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Vowel Count:", count)