line = input("Enter a line of text: ")
words = line.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)
