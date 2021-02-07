import sys
from math import gcd
sys.stdin = open('백준3036. 링.txt', 'r')

N = int(input())
first_ring, *rings = list(map(int, sys.stdin.readline().split()))

for ring in rings:
    print('{}/{}'.format(first_ring//gcd(first_ring, ring), ring//gcd(first_ring, ring)))