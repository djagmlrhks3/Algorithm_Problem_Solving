import sys
sys.stdin = open('백준20953. 고고학자 예린.txt', 'r')

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    total = a+b
    print(total * (total-1) * total // 2)