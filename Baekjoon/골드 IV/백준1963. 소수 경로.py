import sys
from collections import deque
sys.stdin = open('백준1963. 소수 경로.txt', 'r')

def bfs():
    global start, end, answer
    visited = [0] * 9000
    visited[int(start)-1000] = 1
    queue = deque([start])
    while queue:
        s = queue.popleft()
        for i in '0123456789':
            test = [i+s[1:], s[0]+i + s[2:], s[:2]+i + s[-1], s[:3]+i]
            for t in test:
                num = int(t)
                if 1000 <= num <= 9999 and not visited[num-1000] and not DP[num]:
                    if t == end:
                        answer = visited[int(s)-1000]
                        return
                    visited[num-1000] = visited[int(s)-1000]+1
                    queue.append(t)

DP = [0] * 10000
for i in range(2, int(len(DP) ** (0.5))):
    if not DP[i]:
        for j in range(i*2, 10000, i):
            DP[j] = 1
T = int(input())
for _ in range(T):
    answer = -1
    start, end = input().split()
    if start == end:
        answer = 0
    bfs()
    print("Impossible") if answer == -1 else print(answer)