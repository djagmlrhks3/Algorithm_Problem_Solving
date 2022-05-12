import sys, heapq
sys.stdin = open('백준1655. 가운데를 말해요.txt', 'r')

N = int(input())
left, right = [], []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    if left and right and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, -heapq.heappop(left))
    print(-left[0])