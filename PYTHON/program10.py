text = input("Enter text: ")

digit_count = 0
space_count = 0

for character in text:
    if character.isdigit():
        digit_count += 1
    elif character == " ":
        space_count += 1

print("Digits:", digit_count)
print("Spaces:", space_count)