text = input("Enter a string: ")

if text:
    result = text[0] + text[1:].replace(text[0], "$")
else:
    result = ""

print("Result:", result)
