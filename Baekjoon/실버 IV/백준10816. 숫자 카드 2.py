import sys
from bisect import bisect_left, bisect_right
sys.stdin = open('백준10816. 숫자 카드 2.txt', 'r')

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
targets = list(map(int, sys.stdin.readline().split()))
answer = [bisect_right(cards, t) - bisect_left(cards, t) for t in targets]
print(' '.join(map(str, answer)))