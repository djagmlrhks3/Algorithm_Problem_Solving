import sys, heapq
sys.stdin = open('백준11286. 절댓값 힙.txt', 'r')

N = int(input())
heap = []
for _ in range(N):
    num = sys.stdin.readeline()
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
