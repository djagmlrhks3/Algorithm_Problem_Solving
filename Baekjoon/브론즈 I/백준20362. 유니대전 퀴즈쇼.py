import sys
sys.stdin = open('백준20362. 유니대전 퀴즈쇼.txt', 'r')

N, S = input().split()
cnt = dict()
for _ in range(int(N)):
    nick, ans = sys.stdin.readline().split()
    if ans not in cnt.keys():
        cnt[ans] = 1
    else:
        cnt[ans] += 1
    if nick == S:
        print(cnt[ans]-1)
        break