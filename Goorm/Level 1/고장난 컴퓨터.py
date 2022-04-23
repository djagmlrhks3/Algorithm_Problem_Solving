from collections import deque
N, c = map(int, input().split())
candidates = deque(list(map(int, input().split())))
result = []
while candidates:
	if not result:
		result.append(candidates.popleft())
		continue
	if candidates[0] - result[-1] <= c:
		result.append(candidates.popleft())
		continue
	else:
		result.clear()
print(len(result))