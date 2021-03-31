import sys
from collections import deque
sys.stdin = open('백준2251. 물통.txt', 'r')

value = list(map(int, input().split()))
visited = [[0, 0, value[2]]]
queue = deque([[0, 0, value[2]]])
while queue:
    arr = queue.popleft()
    for i in range(3):
        if arr[i]:
            for j in range(3):
                if i == j: continue
                if value[j] - arr[j]:
                    temp = arr[::]
                    test = temp[i] + temp[j]
                    if test > value[j]: # 넘치는 경우
                        temp[i] = test - value[j]
                        temp[j] = value[j]
                    else: # 넘치지 않는 경우
                        temp[j] += temp[i]
                        temp[i] = 0
                    if temp not in visited:
                        visited.append(temp)
                        queue.append(temp)

answer = []
for a, b, c in visited:
    if a == 0 and c not in answer:
        answer.append(c)
answer.sort()
print(' '.join(map(str, answer)))