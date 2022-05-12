import sys
sys.stdin = open('백준15989. 1, 2, 3 더하기 4.txt', 'r')
DP = [[0] * 3 for _ in range(10001)]
DP[1], DP[2], DP[3] = [1, 0, 0], [1, 1, 0], [1, 1, 1]
for idx in range(4, len(DP)):
    DP[idx] = [sum(DP[idx-1][:1]), sum(DP[idx-2][:2]), sum(DP[idx-3])]

for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    print(sum(DP[n]))
