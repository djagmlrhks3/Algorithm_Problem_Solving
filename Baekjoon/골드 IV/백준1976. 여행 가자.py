import sys
sys.stdin = open('백준1976. 여행 가자.txt', 'r')

def find_parents(x):
    if x != parents[x]:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union_parents(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N = int(input())
M = int(input())
parents = [i for i in range(N)]
for start in range(N):
    cities = list(map(int, sys.stdin.readline().split()))
    for end in range(N):
        if cities[end]:
            if find_parents(start) != find_parents(end):
                union_parents(start, end)
plan = list(map(int, sys.stdin.readline().split()))

compare = parents[plan[0]-1]
for num in plan:
    if parents[num-1] != compare:
        print("NO")
        break
else:
    print("YES")