import sys
sys.stdin = open('백준1476. 날짜 계산.txt', 'r')

E, S, M = map(int, input().split())
year = 1
e, s, m = 1, 1, 1
while True:
    if e == E and s == S and m == M:
        break
    e = (e+1) % 16
    s = (s+1) % 29
    m = (m+1) % 20
    year += 1
    if e == 0: e = 1
    if s == 0: s = 1
    if m == 0: m = 1
print(year)