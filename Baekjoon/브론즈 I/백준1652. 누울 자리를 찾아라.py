import sys
sys.stdin = open('백준1652. 누울 자리를 찾아라.txt', 'r')

N = int(input())
room = [sys.stdin.readline() for _ in range(N)]

length, width = 0, 0

for row in room:
    cnt = 0
    for idx in range(N):
        if row[idx] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                length += 1
            cnt = 0
    if cnt >= 2:
        length += 1

for col in range(N):
    cnt = 0
    for row in range(N):
        if room[row][col] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                width += 1
            cnt = 0
    if cnt >= 2:
        width += 1

print(length, width)