words = input("Enter words separated by spaces: ").split()

if not words:
    print("No words entered.")
else:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
