import sys
sys.stdin = open('백준1747. 소수&팰린드롬.txt', 'r')

def check(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True

N = int(input())

if N == 1: N += 1
while True:
    if str(N) == str(N)[::-1]:
        if check(N):
            break
    N += 1
print(N)