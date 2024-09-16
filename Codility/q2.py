# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    m, n = 3, 3
    res = [float('inf')]
    vacant = []  # to store cell indices that have 0 stones
    extra = []  # cell indices with surplus stones
    # populate 'vacant' and 'extra' lists
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                vacant.append((i, j))
            elif A[i][j] > 1:
                for t in range(1, A[i][j]):  # store as many instances of a cell as many surplus stones
                    extra.append((i, j))
    # Note: size of 'vacant' and 'extra' lists would be the same
    backtrack(0, extra, vacant, 0, set())
    if not vacant:  # if all cells have exactly one stone
        return 0
    return res[0]


def backtrack(i, extra, vacant, moves, vis, res):
    if i == len(extra):  # compare and store ans, when leaf node is hit, ie, no cell has surplus stone
        res[0] = min(res[0], moves)
        return

    # Intuitively, sending current surplus stone - stone[i] to each of the vacant positions one by one.
    for k in range(len(vacant)):
        if k not in vis:
            sendto = vacant[k]
            vis.add(k)  # the visited set to store the cells that were in 'vacant' list but now have been occupied
            m = abs(extra[i][0] - sendto[0]) + abs(
                extra[i][1] - sendto[1])  # moves to send stone to vacant cell = manhattan distance
            backtrack(i + 1, extra, vacant, moves + m, vis)
            vis.remove(k)  # the ith stone has been removed from the vacant spot to make available for other stones.
