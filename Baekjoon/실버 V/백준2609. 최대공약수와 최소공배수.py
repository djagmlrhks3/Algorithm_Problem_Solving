import sys
from math import gcd

sys.stdin = open('백준2609. 최대공약수와 최소공배수.txt', 'r')

A, B = map(int, input().split())

print(gcd(A, B))
print(gcd(A, B) * A//gcd(A, B) * B//gcd(A, B))