import sys
from math import gcd

sys.stdin = open('백준9613. GCD 합.txt', 'r')

for _ in range(int(input())):
    n, *args = map(int, sys.stdin.readline().split())
    temp = 0
    for i in range(n-1):
        for j in range(i+1, n):
            temp += gcd(args[i], args[j])
    print(temp)
