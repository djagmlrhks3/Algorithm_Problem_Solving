import sys
sys.stdin = open('백준13305. 주유소.txt', 'r')

N = int(input())
roads = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))
answer = roads[0] * costs[0]
now = costs[0]
for idx in range(1, N-1):
    if costs[idx] < now:
        answer += (costs[idx] * roads[idx])
        now = costs[idx]
    else:
        answer += now * roads[idx]
print(answer)