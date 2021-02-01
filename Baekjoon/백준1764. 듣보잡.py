import sys
sys.stdin = open('백준1764. 듣보잡.txt', 'r')

N, M = map(int, input().split())

not_hear = [input() for _ in range(N)]
not_listen = [input() for _ in range(M)]

res = sorted(list(set(not_hear) & set(not_listen)))

print(len(res))
for people in res:
    print(people)