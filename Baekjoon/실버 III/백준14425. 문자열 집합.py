import sys
sys.stdin = open('백준14425. 문자열 집합.txt', 'r')

N, M = map(int, input().split())
origin, compare = [], dict()

for _ in range(N):
    origin.append(input())
for _ in range(M):
    word = input()
    if word not in compare.keys():
        compare[word] = 1
    else:
        compare[word] += 1

answer = 0

for word, cnt in compare.items():
    if word in origin:
        answer += cnt
print(answer)