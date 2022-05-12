# DP
def solution(m, n, puddles):
    matrix = [[0] * n for _ in range(m)]
    for puddle in puddles:
        matrix[puddle[0] - 1][puddle[1] - 1] = -1

    for c in range(1, n):
        if matrix[0][c] == 0:
            matrix[0][c] = 1
        else:
            break
    for r in range(1, m):
        if matrix[r][0] == 0:
            matrix[r][0] = 1
        else:
            break

    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == -1: continue
            l_t = [matrix[row - 1][col], matrix[row][col - 1]]
            matrix[row][col] = sum(l_t) + l_t.count(-1)
    return matrix[m - 1][n - 1] % 1000000007

# DP + DFS
def solution(m, n, puddles):
    DP = [[0] * m for _ in range(n)]
    d = [(1, 0), (0, 1)]

    def dfs(r, c):
        if r == n - 1 and c == m - 1:
            return 1
        if DP[r][c]:
            return DP[r][c]
        for idx in range(2):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if [nc + 1, nr + 1] in puddles:
                continue
            if nr < n and nc < m:
                DP[r][c] += dfs(nr, nc)
        return DP[r][c]
    return dfs(0, 0) % 1000000007

solution(4, 3, [[2, 2]])