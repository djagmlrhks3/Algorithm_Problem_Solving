import sys
sys.stdin = open('백준1205. 등수 구하기.txt', 'r')

N, T, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, sys.stdin.readline().split()))
    scores.append(T)
    scores.sort(reverse=True)
    temp = scores.index(T) + 1
    if temp > P or (N == P and scores[-1] == T):
        print(-1)
    else:
        print(temp)