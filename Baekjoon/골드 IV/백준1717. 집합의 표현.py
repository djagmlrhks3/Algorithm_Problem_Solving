import sys
sys.stdin = open('백준1717. 집합의 표현.txt', 'r')
sys.setrecursionlimit(10 ** 6)

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

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    order, a, b = map(int, sys.stdin.readline().split())
    if order:
        if find_parents(a) == find_parents(b):
            print("YES")
        else:
            print("NO")
    else:
        union_parents(a, b)