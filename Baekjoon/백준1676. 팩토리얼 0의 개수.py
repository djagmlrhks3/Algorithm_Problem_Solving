import sys
sys.stdin = open('백준1676. 팩토리얼 0의 개수.txt', 'r')

N = int(input())

num = 1
for n in range(2, N+1):
    num *= n

cnt = 0
for number in str(num)[::-1]:
    if number == '0': cnt += 1
    else: break

print(cnt)