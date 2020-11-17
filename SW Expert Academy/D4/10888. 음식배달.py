import sys
sys.stdin = open('sampleinput.txt', 'r')

"""
0 빈 곳
1 집
2 가게(운영비)
"""

def calculate(candidate):
    global house
    result = 0
    for h in house:
        minimum = 0xfffff
        for c in candidate:
            if abs(h[0]-c[0]) + abs(h[1]-c[1]) < minimum:
                minimum = abs(h[0]-c[0]) + abs(h[1]-c[1])
        result += minimum
    return result

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stores = []
    house = []
    res = 0xffffffffff
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2:
                stores.append((i, j))
            if matrix[i][j] == 1:
                house.append((i, j))
    for i in range(1, 1 << len(stores)):
        candidate = []
        before = 0
        for j in range(len(stores)):
            if i & (1 << j):
                candidate.append(stores[j])
                before += matrix[stores[j][0]][stores[j][1]]
        before += calculate(candidate)
        if before < res:
            res = before
    print('#{} {}'.format(tc+1, res))