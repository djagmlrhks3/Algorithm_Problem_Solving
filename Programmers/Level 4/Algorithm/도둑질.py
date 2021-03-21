def solution(money):
    DP1 = [0] * (len(money) - 1)
    DP1[0], DP1[1] = money[0], max(money[0], money[1])
    for idx in range(2, len(money) - 1):
        DP1[idx] = max(DP1[idx - 1], money[idx] + DP1[idx - 2])

    DP2 = [0] * len(money)
    DP2[0], DP2[1] = 0, money[1]
    for idx in range(2, len(money)):
        DP2[idx] = max(DP2[idx - 1], money[idx] + DP2[idx - 2])

    return max(DP1[-1], DP2[-1])