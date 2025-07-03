def minimumPassesOfMatrix(matrix):
    nextPassQueue = []
    passed = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                nextPassQueue.append((row, col))

    while nextPassQueue:
        currQueue = nextPassQueue
        nextPassQueue = []
        while currQueue:
            row, col = currQueue.pop(0)

            if 0 <= row-1 < len(matrix) and matrix[row-1][col] < 0:
                matrix[row-1][col] = matrix[row-1][col] * -1
                nextPassQueue.append((row-1, col))

            if 0 <= row+1 < len(matrix) and matrix[row+1][col] < 0:
                matrix[row+1][col] = matrix[row+1][col] * -1
                nextPassQueue.append((row+1, col))

            if 0 <= col-1 < len(matrix[0]) and matrix[row][col-1] < 0:
                matrix[row][col-1] = matrix[row][col-1] * -1
                nextPassQueue.append((row, col-1))
            
            if 0 <= col+1 < len(matrix[0]) and matrix[row][col+1] < 0:
                matrix[row][col+1] = matrix[row][col+1] * -1
                nextPassQueue.append((row, col+1))

        passed += 1


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] < 0:
                return - 1
    return passed - 1