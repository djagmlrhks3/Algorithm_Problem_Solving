import sys
from collections import deque
sys.stdin = open('백준9205. 맥주 마시면서 결어가기.txt', 'r')
def distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

def bfs():
    global beer, answer, festival_r, festival_c

    while queue:
        r, c = queue.popleft()
        if distance(r, c, festival_r, festival_c) <= 1000:
            answer = True
            return
        for _ in range(len(store)):
            nr, nc = store.popleft()
            if distance(r, c, nr, nc) <= 1000:
                queue.append((nr, nc))
            else:
                store.append((nr, nc))

t = int(input())
for _ in range(t):
    n = int(input())
    answer = False
    start, end = map(int, input().split())
    queue = deque([(start, end)])
    store = deque([])
    beer = 20 * 50
    for _ in range(n):
        s, e = map(int, input().split())
        store.append((s, e))
    festival_r, festival_c = map(int, input().split())
    bfs()
    print("happy") if answer else print("sad")