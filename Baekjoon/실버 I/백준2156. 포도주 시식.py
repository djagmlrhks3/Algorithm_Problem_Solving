import sys
sys.stdin = open('백준2156. 포도주 시식.txt', 'r')
n = int(input())
drinks = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
if n < 3:
    print(sum(drinks))
else:
    DP = [0] * len(drinks)
    DP[0], DP[1], DP[2] = drinks[0], drinks[0]+drinks[1], max(drinks[0] + drinks[1], drinks[0] + drinks[2], drinks[1] + drinks[2])
    for idx in range(3, n):
        DP[idx] = max(drinks[idx] + DP[idx-2], DP[idx-1], drinks[idx] + drinks[idx-1] + DP[idx-3])
    print(DP[-1])