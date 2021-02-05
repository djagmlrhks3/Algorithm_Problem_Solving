import sys
sys.stdin = open('백준1026. 보물.txt', 'r')

N = int(input())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

answer = 0
for idx in range(N):
    answer += (A[idx] * B[idx])
print(answer)