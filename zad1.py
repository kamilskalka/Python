#Napisac program realizujacy mnozenie macierzy (gdzie macierze sa reprezentowane przez listy)


#matrix[row][column]
def dot_product(a,b):
    val = 0
    for i in range(len(a)):
        val = val + a[i]*b[i]
    return val


def matrix_multi(a,b):

    a_height = len(a)
    b_height = len(b)
    b_length = len(b[0])
    b_col = [0] * b_height
    matrix = [[0] * b_length for _ in range(a_height)]

    for i in range(a_height): #row
        for j in range(b_length): #column
            b_col = [b[k][j] for k in range(b_height)]
            matrix[i][j] = dot_product(a[i],b_col)


    return matrix

matrix_a = [[1, 2, 3,-7],
            [3, 2, 1,7]]
matrix_b = [[5, 6,-1],
            [4, -6,-1],
            [1,1,-1],
            [-2,4,-1]]

matrix_c = matrix_multi(matrix_a,matrix_b)
print("matrix:")
for sublist in matrix_c:
    print(sublist)

