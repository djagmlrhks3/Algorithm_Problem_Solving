import sys
sys.stdin = open('백준1874. 스택 수열.txt', 'r')

n = int(input())
stack = []
res = ''
now = 1
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        res += '+'
        now += 1
    if stack[-1] == num:
        stack.pop()
        res += '-'
    else:
        print("NO")
        break
else:
    for r in res:
        print(r)