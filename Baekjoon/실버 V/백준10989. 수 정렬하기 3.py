import sys
sys.stdin = open('백준10989. 수 정렬하기 3.txt', 'r')
N = int(input())
cnt = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    cnt[num] += 1

for idx in range(len(cnt)):
    if cnt[idx]:
        for c in range(cnt[idx]):
            print(idx)