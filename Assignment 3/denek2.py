num_rows = 8
num_columns = 15

# Initialize the matrix with X's for all seats
matrix = []
for i in range(num_rows):
    matrix.append(['X'] * num_columns)

# Print the matrix
for i in range(num_rows):
    # Print the letters for the first column
    print(chr(64+num_rows-i), end=' ')

    # Print the matrix row
    for j in range(num_columns):
        print(matrix[i][j], end=' ')

    # Print a newline character
    print()

# Print the numbers for the last row
print('  ', end='')
for i in range(num_columns):
    print(i, end=' ')