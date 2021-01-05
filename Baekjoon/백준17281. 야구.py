import sys
from itertools import permutations
sys.stdin = open('백준17281. 야구.txt', 'r')

def solve(li):
    score = 0
    idx = 0
    for play in players:
        base1, base2, base3 = 0, 0, 0
        out = 0
        while out < 3:
            if play[li[idx]] == 0:
                out += 1
            elif play[li[idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif play[li[idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif play[li[idx]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif play[li[idx]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            idx = (idx+1) % 9
    return score

N = int(sys.stdin.readline())
players = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
for li in permutations(i for i in range(1, 9)):
    answer = max(answer, solve(list(li[:3]) + [0] + list(li[3:])))
print(answer)