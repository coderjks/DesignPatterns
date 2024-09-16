# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    n = len(A)
    m = len(A[0])
    solution_cell = 0

    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                # start dfs from this position
                dfs(i, j, i, j, n, m, K, A)

    for row in A:
        for cell in row:
            if cell == 0:
                solution_cell += 1

    print(A)
    return solution_cell


def dfs(x, y, i, j, n, m, k, visited):
    if i < 0 or i >= n:
        return

    if j < 0 or j >= m:
        return

    if abs(x - i) + abs(y - j) > k:
        return

    if visited[i][j] in (0, 1):
        # print(x, y, i, j)
        if visited[i][j] == 0:
            visited[i][j] = 2

            # go right
            dfs(x, y, i, j + 1, n, m, k, visited)

            # left
            dfs(x, y, i, j - 1, n, m, k, visited)

            # up
            dfs(x, y, i - 1, j, n, m, k, visited)

            # down
            dfs(x, y, i + 1, j, n, m, k, visited)

            # dig down right & left
            dfs(x, y, i + 1, j + 1, n, m, k, visited)
            dfs(x, y, i + 1, j - 1, n, m, k, visited)

            # dig up right & left
            dfs(x, y, i - 1, j + 1, n, m, k, visited)
            dfs(x, y, i - 1, j - 1, n, m, k, visited)


A = [[1, 0, 0], [0, 0, 0], [0, 0, 1], [0, 1, 0]]

print(solution(A, 1))
