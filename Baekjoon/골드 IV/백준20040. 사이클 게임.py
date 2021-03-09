import sys
sys.stdin = open('백준20040. 사이클 게임.txt', 'r')

def find_parent(x):
    if x != parents[x]:
        return find_parent(parents[x])
    return x

def union_parent(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 < n2:
        parents[n2] = n1
    else:
        parents[n1] = n2

n, m = map(int, input().split())
parents = [i for i in range(n)]
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

for idx, info in enumerate(edges):
    if find_parent(info[0]) != find_parent(info[1]):
        union_parent(info[0], info[1])
    else:
        print(idx+1)
        break
else:
    print(0)