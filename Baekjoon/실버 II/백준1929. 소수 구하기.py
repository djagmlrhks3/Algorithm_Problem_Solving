import sys
sys.stdin = open('백준1929. 소수 구하기.txt', 'r')


M, N = map(int, input().split())
candidates = [False, False] + [True] * (N-1)

for num in range(2, N//2 + 1):
    if candidates[num]:
        for idx in range(2*num, N+1, num):
            candidates[idx] = False

for num in range(M, N+1):
    if candidates[num]:
        print(num)