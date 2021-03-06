import sys, heapq
sys.stdin = open('백준11279. 최대 힙.txt', 'r')

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num:
        heapq.heappush(heap, -num)
    else:
        if heap:
            print(abs(heapq.heappop(heap)))
        else:
            print(0)