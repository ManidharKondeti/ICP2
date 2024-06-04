rows = 5
for i in range(1, rows * 2):
    if i <= rows:
        # For the upper half of the pyramid
        print("* " * i)
    else:
        # For the lower half of the pyramid
        print("* " * (2 * rows - i))

