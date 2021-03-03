import sys, heapq
sys.stdin = open('백준13549. 숨바꼭질 3.txt', 'r')

N, K = map(int, input().split())
check = [int(1e9)] * 100001
check[N] = 0
heap = []
heapq.heappush(heap, (0, N))

while heap:
    move, idx = heapq.heappop(heap)
    if check[K] != int(1e9):
        break
    for value in [idx*2, idx-1, idx+1]:
        if 0 <= value < 100001:
            if check[value] == int(1e9) and idx*2 == value:
                heapq.heappush(heap, (move, value))
                check[value] = move
            elif check[value] == int(1e9):
                heapq.heappush(heap, (move+1, value))
                check[value] = move+1
print(check[K])
