import sys
sys.stdin = open('백준14725. 개미굴.txt', 'r')
routes = []

for _ in range(int(input())):
    K, *li = sys.stdin.readline().split()
    routes.append(li)
routes.sort()

start = ''
for r in range(len(routes)):
    if routes[r][0] != start:
        start = routes[r][0]
        print(start)
        res = ''
        for idx in range(1, len(routes[r])):
            res += '--'
            print(res + routes[r][idx])
    else:
        cnt = 0
        for idx in range(1, len(routes[r])):
            if idx < len(routes[r-1]) and routes[r-1][idx] == routes[r][idx]:
                cnt += 1
            else:
                break
        for idx in range(cnt+1, len(routes[r])):
            print('--'*idx + routes[r][idx])