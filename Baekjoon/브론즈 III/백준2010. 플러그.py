import sys
sys.stdin = open('백준2010. 플러그.txt', 'r')

N = int(input())
answer = 0
for _ in range(N):
    answer += int(input())

print(answer - (N-1))