import sys
sys.stdin = open('백준9372. 상근이의 여행.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # 국가의 수 / 비행기의 종류
    for _ in range(M): trash = sys.stdin.readline()
    print(N-1)