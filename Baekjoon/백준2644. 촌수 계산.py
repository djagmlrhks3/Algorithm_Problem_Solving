import sys
sys.stdin = open('백준2644. 촌수 계산.txt', 'r')

def solution(h1):
    global h2
    step = 0
    queue = list()
    queue.append(h1)
    check[h1] = 1
    while len(queue):
        step += 1
        for i in range(len(queue)):
            start = queue.pop(0)
            if start == h2:
                step -= 1
                return step
            for j in people[start]:
                if not check[j]:
                    check[j] = 1
                    queue.append(j)
    return -1
n = int(input())
h1, h2 = map(int,input().split())
M = int(input())
people = [[] for _ in range(n+1)]
for m in range(M):
    x, y = map(int,input().split())
    people[x].append(y)
    people[y].append(x)
check = [0]*(n+1)
print(people)
print(solution(h1))