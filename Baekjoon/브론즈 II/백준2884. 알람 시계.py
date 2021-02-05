import sys
sys.stdin = open('백준2884. 알람 시계.txt','r')

T = int(input())
for tc in range(T):
    H, M = map(int,input().split())
    if M >= 45:
        print(H, end=" ");print(M-45)
    else:
        M = 60 - (45-M)
        H -= 1
        if H < 0:
            H = 23
    print(H, end=" ");print(M)