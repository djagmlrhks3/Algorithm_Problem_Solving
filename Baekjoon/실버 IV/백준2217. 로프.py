import sys
sys.stdin = open('백준2217. 로프.txt', 'r')

N = int(input())
ropes = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
answer = ropes[0]
for idx in range(1, N):
    if answer < ropes[idx] * (idx+1):
        answer = ropes[idx] * (idx+1)
print(answer)