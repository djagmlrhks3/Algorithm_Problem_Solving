import sys
sys.stdin = open('백준1748. 수 이어 쓰기 1.txt', 'r')
N = int(input())
answer = 0
for n in range(len(str(N))-1, -1, -1):
    cnt = ((N // 10 ** n) - 1) * (10 ** n) + (N % 10 ** n) + 1
    N -= cnt
    answer += cnt * (n+1)
print(answer)