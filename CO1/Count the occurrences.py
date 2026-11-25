line = input("Enter a line of text: ")

words = line.split()

for word in set(words):
    print(word, ":", words.count(word))