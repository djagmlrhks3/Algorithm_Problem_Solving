import sys
sys.stdin = open('백준2565. 전깃줄.txt', 'r')

N = int(input())
candidates = []
for _ in range(N):
    A, B = map(int, input().split())
    candidates.append((A, B))

candidates = sorted(candidates, key=lambda x:(x[0]))

LIS = [1] * len(candidates)
for i in range(1, len(LIS)):
    for j in range(i):
        if candidates[i][1] > candidates[j][1]:
            LIS[i] = max(LIS[i], LIS[j]+1)
print(N - max(LIS))
