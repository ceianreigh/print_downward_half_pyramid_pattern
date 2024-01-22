# Print a downward Half-Pyramid Pattern of Star (asterisk)

# pseudocode

# using nested for loop
# outer loop for number of rows
for i in range(5):
    # inner loop for number of columns
    for j in range(5 - i):
        # print star
        (print("*", end=" "))
    # print new line after inner loop
    print()
