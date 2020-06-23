import sys
sys.stdin = open('5248. 그룹 나누기.txt','r')

def make_set(x):
    p[x] = x
def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]
def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        for i in range(1,len(p)):
            if p[i] == py:
                p[i] = px
        rank[px] += 1
    else:
        for i in range(1,len(p)):
            if p[i] == px:
                p[i] = py
        if rank[px] == rank[py]:
            rank[py] += 1

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    couples = list(map(int, input().split()))
    p = [0] * (N+1)
    rank = [0]*(N+1)
    for i in range(N+1):
        make_set(i)
    for m in range(M):
        a, b = couples[2*m], couples[2*m+1]
        union(a, b)
    print('#{} {}'.format(tc+1, len(set(p))-1))