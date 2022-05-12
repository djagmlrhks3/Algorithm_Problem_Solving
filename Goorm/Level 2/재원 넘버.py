n = int(input())
DP = [0] * n
for i in range(1, n+1):
	DP[i-1] = 3 ** i
print(sum(DP))