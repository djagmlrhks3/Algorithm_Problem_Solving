import sys
from math import gcd
sys.stdin = open('백준1735. 분수 합.txt', 'r')

As, Am = map(int, input().split())
Bs, Bm = map(int, input().split())

Ns = As * Bm + Bs * Am
Nm = Am * Bm

while True:
    GCD = gcd(Ns, Nm)
    if GCD == 1:
        break
    else:
        Ns //= GCD
        Nm //= GCD
print(Ns, Nm)