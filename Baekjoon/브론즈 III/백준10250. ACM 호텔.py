import sys
sys.stdin = open('백준10250. ACM 호텔.txt', 'r')

# 간단한 수학문제 - 나머지, 몫이 0일 때만 주의하면 된다.
T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        row = H
        col = (N // H)
    else:
        row = N % H
        col = (N // H) + 1

    print(str(row) + '0' + str(col)) if col < 10 else print(str(row) + str(col))