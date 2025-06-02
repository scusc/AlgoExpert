def transposeMatrix(matrix):
    resRows = len(matrix[0])
    resCols = len(matrix)
    
    res = [[0]*resCols for _ in resRows]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]

    return res