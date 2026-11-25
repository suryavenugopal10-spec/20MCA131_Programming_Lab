data = {"b": 20, "a": 10, "d": 40, "c": 30}

ascending = dict(sorted(data.items()))
descending = dict(sorted(data.items(), reverse=True))

print("Original dictionary:", data)
print("Ascending order:", ascending)
print("Descending order:", descending)
