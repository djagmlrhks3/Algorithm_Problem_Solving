#1. deque 사용
from collections import deque
before = deque(list(''.join(input().rstrip())))
after = []
after.append(before.popleft())
while before:
	if after[-1] > before[0]:
		after.pop()
		break
	else:
		after.append(before.popleft())
else:
	after.pop()
print(''.join(after + list(before)))

#2 단순 반복문
original = input().rstrip()
length = len(original)
now, idx = original[0], -1
name = ''
for i in range(1, length):
	if now > original[i]:
		idx = i
		break
	else:
		name += now
		now = original[i]
if idx == -1:
	name = name[:length]
else:
	for i in range(idx, length):
		name += original[i] 
print(name)