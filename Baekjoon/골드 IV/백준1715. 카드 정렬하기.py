import sys, heapq
sys.stdin = open('백준1715. 카드 정렬하기.txt', 'r')

N = int(input())
heap = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(heap)
print(heap)
if N == 1:
    print(heap[0])
else:
    answer = 0
    while len(heap) > 1:
        card1 = heapq.heappop(heap)
        card2 = heapq.heappop(heap)
        answer += (card1 + card2)
        heapq.heappush(heap, card1 + card2)
    print(answer)