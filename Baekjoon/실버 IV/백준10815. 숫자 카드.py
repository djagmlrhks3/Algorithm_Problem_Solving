import sys
from bisect import bisect_left
sys.stdin = open('백준10815. 숫자 카드.txt', 'r')
N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
targets = list(map(int, sys.stdin.readline().split()))
res = []
for t in targets:
    if t <= max(cards):
        idx = bisect_left(cards, t)
        if cards[idx] == t:
            res.append(1)
        else:
            res.append(0)
    else:
        res.append(0)
print(' '.join(map(str, res)))