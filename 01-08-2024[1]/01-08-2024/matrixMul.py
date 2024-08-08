def read_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def main():
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    matrix1 = read_matrix(rows1, cols1)

    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))
    matrix2 = read_matrix(rows2, cols2)

    try:
        result = matrix_multiplication(matrix1, matrix2)
        print("The resulting matrix after multiplication is:")
        print_matrix(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
