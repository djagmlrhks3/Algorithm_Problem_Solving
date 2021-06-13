import sys
sys.stdin = open('백준21921. 블로그.txt', 'r')

N, X = map(int, sys.stdin.readline().split())
visit = list(map(int, sys.stdin.readline().split()))
candidate = sum(visit[:X])
result = candidate
cnt = 1
for i in range(X, len(visit)):
    candidate -= visit[i-X]
    candidate += visit[i]
    if candidate > result:
        result = candidate
        cnt = 1
    elif result == candidate:
        cnt += 1
if result:
    print(result)
    print(cnt)
else:
    print("SAD")