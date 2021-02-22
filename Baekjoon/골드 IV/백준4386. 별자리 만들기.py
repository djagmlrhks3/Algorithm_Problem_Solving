import sys, heapq
sys.stdin = open('백준4386. 별자리 만들기.txt', 'r')

def calculate(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** (0.5)

def find_parent(start):
    if start != parent[start]:
        return find_parent(parent[start])
    return parent[start]

def union_parent(star1, star2):
    star1 = find_parent(star1)
    star2 = find_parent(star2)
    if star1 < star2:
        parent[star2] = star1
    else:
        parent[star1] = star2

n = int(input())
stars = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

parent = [i for i in range(n)]
costs = []
answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        heapq.heappush(costs, (calculate(stars[i][0], stars[i][1], stars[j][0], stars[j][1]), i, j))

while costs:
    cost, i, j = heapq.heappop(costs)
    if find_parent(i) != find_parent(j):
        union_parent(i, j)
        answer += cost
print(round(answer, 2))
