def dfs(row, col, visited, matrix):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])) or (row, col) in visited or matrix[row][col] == 0:
        return 0
    visited.add((row, col))
    size = 0
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for dx, dy in directions:
        size += dfs(row+dx, col+dy, visited, matrix)
    return size + 1


def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    res = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1 and (row, col) not in visited:
                res.append(dfs(row, col, visited, matrix))
    return res