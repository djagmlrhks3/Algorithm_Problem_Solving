N = int(input())
time = []
while N:
	i = 0
	while True:
		if 2**i > N:
			time.append(i-1)
			N -= 2**(i-1)
			break
		else:
			i += 1
print(len(time))
print(' '.join(map(str, sorted(time))))