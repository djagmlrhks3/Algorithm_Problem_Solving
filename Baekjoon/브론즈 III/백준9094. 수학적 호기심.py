import sys
sys.stdin = open('백준9094. 수학적 호기심.txt', 'r')

def check(n, m):
    global res
    for a in range(1, n-1):
        for b in range(a+1, n):
            temp = (a**2 + b**2 + m)/(a*b)
            if int(temp) == temp:
                res += 1

T = int(input())
for tc in range(T):
    res = 0
    n, m = map(int, input().split())
    check(n, m)
    print(res)