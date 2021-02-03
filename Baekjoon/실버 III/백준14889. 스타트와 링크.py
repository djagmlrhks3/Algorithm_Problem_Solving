import sys
sys.stdin = open('백준14889. 스타트와 링크.txt', 'r')
from itertools import combinations

def solve(li):
    global answer
    s = li
    l = list(set(all) - set(li))
    start_ability, link_ability = 0, 0

    for pair in combinations(s, 2):
        start_ability += people[pair[0]][pair[1]]
        start_ability += people[pair[1]][pair[0]]
    for pair in combinations(l, 2):
        link_ability += people[pair[0]][pair[1]]
        link_ability += people[pair[1]][pair[0]]

    answer = min(answer, abs(start_ability-link_ability))

N = int(input())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = int(1e9)
all = [i for i in range(N)]
for li in combinations(all, N//2):
    solve(li)
print(answer)