import sys
sys.stdin = open('백준11723. 집합.txt', 'r')

S = set()
for _ in range(int(input())):
    given = input().split()
    if len(given) > 1: num = int(given[1])
    if given[0] == 'all': S = {i for i in range(1, 21)}
    elif given[0] == 'empty': S.clear()
    elif given[0] == 'add': S.add(num)
    elif given[0] == 'remove' and num in S: S.remove(num)
    elif given[0] == 'check':
        if num in S: print(1)
        else: print(0)
    elif given[0] == 'toggle':
        if num in S: S.remove(num)
        else: S.add(num)