N = int(input())
heap = []
numbers = list(map(int, input().split()))
exists = dict()
for num in numbers:
	exists[num] = 1
M = int(input())
candidates = list(map(int, input().split()))
for num in candidates:
	try:
		print(exists[num])
	except:
		print(0)