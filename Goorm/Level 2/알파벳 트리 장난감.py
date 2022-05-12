N = int(input())
alpha = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = dict()
for i in range(1, len(alpha)):
	value[alpha[i]] = i
tree = []
for _ in range(N):
	line = input().rstrip()
	dummy = [int(value[line[i]]) for i in range(len(line))]
	tree.append(dummy)
for i in range(1, N):
	for j in range(2**i):
		tree[i][j] += tree[i-1][j//2]
leaf = sorted(tree[-1])
print(leaf[0])
print(leaf[-1])