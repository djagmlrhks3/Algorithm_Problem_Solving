N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = distance[0] * price[0]
now_idx = 0
for i in range(1, N-1):
	ver1 = price[i] * distance[i]
	ver2 = price[now_idx] * distance[i]
	if ver1 < ver2:
		now_idx = i
	answer += distance[i] * price[now_idx]
print(answer)