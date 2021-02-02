import sys
sys.stdin = open('백준2581. 소수.txt', 'r')

def check(num):
    if num < 2:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True

M = int(input())
N = int(input())

candidates = []
for num in range(M, N+1):
    if check(num):
        candidates.append(num)

if candidates:
    print(sum(candidates))
    print(min(candidates))
else:
    print(-1)