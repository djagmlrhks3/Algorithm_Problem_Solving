import sys
sys.stdin = open('백준11653. 소인수분해.txt', 'r')

N = int(input())
if N >= 1:
    num = 2
    while N > 1:
        if not N % num:
            print(num)
            N //= num
        else:
            num += 1
