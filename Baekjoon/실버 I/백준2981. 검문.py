import sys
sys.stdin = open('백준2981. 검문.txt', 'r')
from math import gcd

N = int(input())
numbers = [int(input()) for _ in range(N)]
candidates = []
res = set()
"""
수식을 만들어 해결방법을 찾는 것이 핵심!
N1 = M x Q1 + R
N2 = M x Q2 + R
N3 = < x Q3 + R
"""
for idx in range(1, N):
    candidates.append(abs(numbers[idx] - numbers[idx-1]))

if len(candidates) == 1: gcd_num = candidates[0]
else: gcd_num = gcd(candidates[0], candidates[1])

for idx in range(2, len(candidates)):
    gcd_num = gcd(gcd_num, candidates[idx] - candidates[idx-1])

res.add(gcd_num)
for num in range(2, int(gcd_num**(0.5))+1): # 최대공약수의 범위로 약수를 구하면 시간초과가 나므로 최대공약수 제곱근의 범위까지 구한다.
    if not gcd_num % num:
        res.add(num)
        res.add(gcd_num//num)
res -= {1} # '1' 제거
print(' '.join(map(str, sorted(list(res)))))