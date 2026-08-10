text = input("Enter text: ")

upper_count = 0
lower_count = 0

for character in text:
    if character.isupper():
        upper_count += 1
    elif character.islower():
        lower_count += 1

print("Uppercase:", upper_count)
print("Lowercase:", lower_count)