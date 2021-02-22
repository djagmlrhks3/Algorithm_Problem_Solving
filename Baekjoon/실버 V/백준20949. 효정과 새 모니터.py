import sys
sys.stdin = open('백준20949. 효정과 새 모니터.txt', 'r')

candidates = []
N = int(input())
for idx in range(1, N+1):
    W, H = map(int, input().split())
    candidates.append((W**2 + H**2, idx))

for ppi, num in sorted(candidates, key=lambda x:(-x[0], x[1])):
    print(num)