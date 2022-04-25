N = int(input())
rams = list(map(int, input().split()))
destroy = []
for i in range(N):
	if (rams[i] & rams[i]-1):
		destroy.append(i+1)
print(len(destroy))
print(' '.join(list(map(str, destroy))))