import sys
sys.stdin = open('백준9375. 패션왕 신해빈.txt', 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = dict()
    for _ in range(N):
        name, kind = map(str, input().split())
        if kind not in clothes.keys():
            clothes[kind] = [name]
        else:
            clothes[kind].append(name)
    answer = 1
    for v in clothes.values():
        answer *= (len(v)+1)
    answer -= 1
    print(answer)