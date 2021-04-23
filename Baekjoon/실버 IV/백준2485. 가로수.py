import sys
sys.stdin = open('백준2485. 가로수.txt', 'r')
from math import gcd

N = int(input())
candidates = []
last = int(input())
for i in range(N - 1):
    num = int(sys.stdin.readline().rstrip())
    candidates.append(num - last)
    last = num

g = candidates[0]
for i in range(1, len(candidates)):
    g = gcd(g, candidates[i])
answer = 0

for c in candidates:
    answer += (c // g) - 1
print(answer)