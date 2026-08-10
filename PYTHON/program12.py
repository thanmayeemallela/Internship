text = input("Enter text: ")

result = ""

for character in text:
    if character not in result:
        result += character

print("Result:", result)