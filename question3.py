x = [23, 'Python', 23.98]

# Initialize an empty list to store the types
types_list = []

# Iterate over each element in the list
for item in x:
    # Append the element to the types_list
    types_list.append(type(item))

# Print the original list
print(x)

# Print the types of elements
print(types_list)
