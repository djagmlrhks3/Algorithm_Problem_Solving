import sys
sys.stdin = open('백준1931. 회의실 배정.txt', 'r')

N = int(input())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

now, answer = 0, 0
for s, e in meetings:
    if s >= now:
        answer += 1
        now = e
print(answer)