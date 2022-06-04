def solution(n):
    DP = [0] * (n+1)
    DP[2] = 3
    for i in range(4, n+1, 2):
        if not i % 2:
            DP[i] = (DP[i-2] * 3 + sum(DP[2:i-3]) * 2 + 2) % 1000000007
    return DP[n]