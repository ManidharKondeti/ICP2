def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    print("No. of Upper-case characters:", upper_count)
    print("No. of Lower-case Characters:", lower_count)

input_string = 'The quick Brow Fox'
count_case(input_string)
