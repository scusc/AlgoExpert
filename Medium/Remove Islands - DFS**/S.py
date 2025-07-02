def traverse(row, col, visited, matrix):
    visited.add((row, col))
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    # if we are at the border, we can return True
    # since we are looking for islands that are not connected to the border
    res = row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) - 1
    for dx, dy in directions:
        nextRow = row + dx
        nextCol = col + dy
        if 0<= nextRow < len(matrix) and 0<= nextCol < len(matrix[0]) and (nextRow, nextCol) not in visited and matrix[nextRow][nextCol] != 0:
            res = res or traverse(nextRow, nextCol, visited, matrix)
    
    # need to backtrack
    # since we are modifying the matrix
    # and we need to mark the cell as not visited again for next iterations
    # so we can continue the search
    visited.remove((row, col))
    return res


def removeIslands(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    visited = set()

    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] != 0:
                matrix[row][col] = int(traverse(row, col, visited, matrix))
    return matrix