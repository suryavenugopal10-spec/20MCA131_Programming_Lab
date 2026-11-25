color_list1 = ['red', 'green', 'blue', 'yellow']
color_list2 = ['green', 'yellow']

result = [color for color in color_list1 if color not in color_list2]

print("Result:", result)