candidates = list(map(int, input().split()))
num1, num2, num3 = 0, 0, 0
for num in candidates:
	if num == 1:
		num1 += 1
	elif num == 2:
		num2 += 1
	else:
		num3 += 1
answer = 0
if num1 and num2 and num3:
	answer = 0
elif num1 and num2:
	answer = num2
elif num2 and num3:
	answer = num3
elif num1 and num3:
	answer = num1
print(answer)
	