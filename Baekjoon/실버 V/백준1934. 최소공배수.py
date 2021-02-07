import sys
from math import gcd

sys.stdin = open('백준1934. 최소공배수.txt', 'r')

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(A//gcd(A, B) * B//gcd(A, B) * gcd(A, B))