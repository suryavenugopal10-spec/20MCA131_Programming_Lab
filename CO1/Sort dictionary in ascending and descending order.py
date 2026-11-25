my_dict = {3: 'Apple', 1: 'Banana', 4: 'Orange', 2: 'Mango'}

ascending = dict(sorted(my_dict.items()))

descending = dict(sorted(my_dict.items(), reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)