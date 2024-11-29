#Napisac program realizujacy mnozenie macierzy (gdzie macierze sa reprezentowane przez listy)

matrix_a = [[1, 2, 5], [3, 4, 2]]
matrix_b = [[5, 6], [7, 8]]

def matrix_multi(a,b):
    a_height = len(a)
    a_length = len(a[0])


    b_height = len(b)
    b_length = len(b[0])


for i in range(b_height):
    for j in range(a_length):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row)
