import sys
sys.stdin = open('백준1759. 암호 만들기.txt', 'r')
from itertools import combinations

L, C = map(int, input().split())
mos = []
jas = []
alphabet = list(map(str, sys.stdin.readline().split()))
for al in alphabet:
    if al in 'aeiou':
        mos.append(al)
    else:
        jas.append(al)

ans = []
for m_idx in range(len(mos)):
    choice_mo = [mos[m_idx]] # 선택한 최소 모음1개
    last_mo = mos[:m_idx] + mos[m_idx+1:] # 나머지 모음들
    for li in combinations(jas, 2):  # 선택한 최소 자음2개
        choice_ja = list(li) # 선태한 최소 자음2개
        last_ja = list(set(jas) - set(li)) # 나머지 자음들
        for la in combinations(last_mo + last_ja, L-3):
            res = ''.join(sorted(choice_mo + choice_ja + list(la)))
            if res not in ans:
                ans.append(res)
for r in sorted(ans):
    print(r)

"""
백트래킹
import sys
sys.stdin = open('백준1759. 암호 만들기.txt', 'r')
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
pwd = sorted(list(map(str, sys.stdin.readline().split())))

comb = combinations(pwd, L)

for c in comb:
    count = 0
    for letter in c:
        if letter in 'aeiou':
            count += 1

    if (count >= 1) and (count <= L-2):
        print(''.join(c))
"""