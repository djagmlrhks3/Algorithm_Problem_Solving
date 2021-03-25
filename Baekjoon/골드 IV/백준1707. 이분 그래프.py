import sys
from collections import deque
sys.stdin = open('백준1707. 이분 그래프.txt')

for idx in range(int(input())):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(1, V+1)}

    for _ in range(E):
        n1, n2 = map(int, sys.stdin.readline().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    answer = "YES"
    check = [-1] * (V+1)
    for n in range(1, V+1):
        queue = deque([])
        if check[n] == -1:
            queue.append(n)
            check[n] = 0
        if answer != "YES":
            break
        while queue:
            n1 = queue.popleft()
            for n2 in adj[n1]:
                if check[n2] == -1:
                    check[n2] = (check[n1] + 1) % 2
                    queue.append(n2)
                else:
                    if check[n1] == check[n2]:
                        answer = "NO"
                        queue.clear()
                        break
    print(answer)