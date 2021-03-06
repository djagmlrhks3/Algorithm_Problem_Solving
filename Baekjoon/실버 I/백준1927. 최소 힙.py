import sys, heapq
sys.stdin = open('백준1927. 최소 힙.txt', 'r')

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if not num:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)