import sys
sys.stdin = open('백준1712. 손익분기점.txt', 'r')

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print((A // (C - B)+1))