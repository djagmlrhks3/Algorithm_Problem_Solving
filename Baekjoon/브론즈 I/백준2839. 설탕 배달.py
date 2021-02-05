import sys
sys.stdin = open('백준2839. 설탕 배달.txt', 'r')

N = int(input())
cnt = 0

while N:
    if not N % 5:
        cnt += N // 5
        break
    N -= 3
    cnt += 1
    if N < 0:
        cnt = -1
        break
print(cnt)