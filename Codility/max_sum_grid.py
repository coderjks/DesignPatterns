def get_max_profit(matrix) -> int:
    n = len(matrix)
    m = len(matrix[0])
    visited = [[0 for _ in range(m)] for __ in range(n)]
    global MAX_PROFIT = float('-inf')

    def dfs_helper(i, j, visited, path, cur_profit):
        if i == n - 1 and j == m - 1:
            # reached the last cell
            # print(path + [(i, j)], cur_profit + matrix[i][j])
            MAX_PROFIT = max(MAX_PROFIT, cur_profit + matrix[i][j])
            return

        if i < 0 or i >= n:
            return

        if j < 0 or j >= m:
            return

        # print(i, j)
        if visited[i][j] == 0 and visited[i][j] != "inf":
            visited[i][j] = 1
            cur_profit += matrix[i][j]
            # down
            dfs_helper(i + 1, j, visited, path + [(i, j)], cur_profit)
            # up
            dfs_helper(i - 1, j, visited, path + [(i, j)], cur_profit)
            # left
            dfs_helper(i, j - 1, visited, path + [(i, j)], cur_profit)
            # right
            dfs_helper(i, j + 1, visited, path + [(i, j)], cur_profit)
            visited[i][j] = 0
            cur_profit -= matrix[i][j]

    dfs_helper(0, 0, visited, [], 0)
    # print(max_profit)
    return max_profit[0]

grid =  [
        [5, -10, 3, 2, -8, 1, 7, -5, 3, 9],
        [6, 4, -3, 1, -2, 10, 5, 8, 2, -1],
        [1, -1, 5, 9, -7, 4, 6, -6, 1, 2],
        [-2, 8, -4, 0, 3, 2, -3, 7, -9, 4],
        [4, 2, 1, -1, 5, 3, 8, -2, 6, 1],
        [3, 6, -5, 4, 7, -9, 1, 2, 0, 5],
        [7, -8, 2, 5, 0, 6, 3, -1, 4, -7],
        [-1, 3, 4, -2, 9, -6, 7, 1, -4, 5],
        [2, 9, -3, 6, 8, -5, 4, 2, 3, -2],
        [8, 1, 2, 0, -4, 5, -6, 9, 1, 6],
        [-3, 7, 0, 5, 2, -1, 8, 4, -7, 3],
        [6, 2, -1, 7, 9, -8, 5, -3, 0, 2],
        [1, 5, 8, -2, 6, 3, 4, 0, 7, -1],
        [9, -4, 2, 3, -5, 8, 1, -9, 2, 4],
        [2, 3, 7, 6, -4, 0, 5, -1, 8, 10]
    ]


print(get_max_profit(grid))