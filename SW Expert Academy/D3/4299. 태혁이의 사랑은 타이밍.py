import sys
sys.stdin = open('4299. 태혁이의 사랑은 타이밍.txt','r')

T = int(input())
for tc in range(T):
    result = 0
    D, H, M = map(int,input().split())
    if D == 11 and H < 11 or D == 11 and H <= 11 and M < 11:
        print('#{} {}'.format(tc+1,-1))
    else:
        if H >= 11 and M >= 11:
            result += (D-11) * 60 * 24
            result += (H-11) * 60
            result += M-11
            print('#{} {}'.format(tc + 1, result))
        elif H < 11 and M >= 11:
            result += (D-12) * 60 * 24
            result += 13 * 60 + H * 60
            result += M-11
            print('#{} {}'.format(tc + 1, result))
        elif H >= 11 and M < 11:
            result += (D-11) * 60 * 24
            result += (H-12) * 60
            result += 49 + M
            print('#{} {}'.format(tc + 1, result))
        elif H < 11 and M < 11:
            result += (D-12) * 60 * 24
            result += 12 * 60 + H * 60
            result += 49 + M
            print('#{} {}'.format(tc + 1, result))