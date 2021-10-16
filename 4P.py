def PrintMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j == len(mat[i]) - 1:
                print(mat[i][j], end = '')
            else:
                print(mat[i][j], end = ' ')
        print()

PrintMatrix([[1, 2, 3], [4, 5, 6]])