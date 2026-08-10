sentence = input("Enter sentence: ")

words = sentence.split()
longest = max(words, key=len)

print("Longest Word:", longest)