N = int(input())
alpha = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = {alpha[i]:i for i in range(1, len(alpha))}
trangle = []
for _ in range(N):
	trangle.append(input().rstrip())
DP = [[0] * (i+1) for i in range(N)]
DP[0][0] = value[trangle[0]]
for r in range(1, N):
	DP[r][0] = DP[r-1][0] + value[trangle[r][0]]
	DP[r][-1] = DP[r-1][-1] + value[trangle[r][-1]]
	for c in range(1, r):
		DP[r][c] = max(DP[r-1][c], DP[r-1][c-1]) + value[trangle[r][c]]	

answer = max(DP[-1])
print(answer)