def transpose_matrix(matrix, i=0, j=0):
    if i == len(matrix):
        return matrix

    # Swap the elements at (i, j) and (j, i) in-place
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Move to the next element in the matrix
    if j == len(matrix[0]) - 1:
        # Move to the next row
        return transpose_matrix(matrix, i + 1, 0)
    else:
        # Move to the next column
        return transpose_matrix(matrix, i, j + 1)

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
def generate_matrix():
    mat_rows = input("Enter amount of rows in matrix: ")
    matrix = []

    for i in range(int(mat_rows)):
        row = input("Enter matrix row: ").split()
        matrix.append(row)

    return matrix

matrix = generate_matrix()

print("Original Matrix:")
print_matrix(matrix)

transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
print_matrix(transposed)