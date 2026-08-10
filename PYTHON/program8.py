text = input("Enter text: ").lower()

vowels = "aeiou"
count = 0

for character in text:
    if character.isalpha() and character not in vowels:
        count += 1

print("Consonant Count:", count)