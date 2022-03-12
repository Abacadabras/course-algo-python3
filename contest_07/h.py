def determinant(matrix, n):
    """
        Function that calculates determinant of given matrix
        of size n x n. Calculation is proceeded using
        first line of matrix.

        Input:

        matrix - matrix of size n x n.
        n - size of matrix.

        Output:

        det - determinant of matrix.
    """
    if n == 0:  # if matrix has 0 size
        return 0
    elif n == 1:  # if matrix is a number
        return matrix[0][0]
    elif n == 2:  # if matrix is 2 x 2
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    else:  # else, using determinant formula
        det = 0
        for i in range(n):
            det += matrix[i][n - 1] * ((-1) ** (i + n -1)) * determinant(matrix[:i] + matrix[i+1:], n-1)
        return det


size = int(input())  # getting matrix from input
matrix = [list(map(int, input().split())) for i in range(size)]
print(determinant(matrix, size))
