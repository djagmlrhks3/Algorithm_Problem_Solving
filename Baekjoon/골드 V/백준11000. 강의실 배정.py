import heapq, sys
sys.stdin = open('백준11000. 강의실 배정.txt', 'r')

N = int(input())

classes = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
classes.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1,N):
    if heap[0] > classes[i][0]:
        heapq.heappush(heap, classes[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])
print(len(heap))
