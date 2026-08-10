text = input("Enter text: ")

for character in text:
    if text.count(character) == 1:
        print("First Non-Repeated Character:", character)
        break