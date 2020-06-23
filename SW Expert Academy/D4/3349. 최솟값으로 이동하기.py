import sys
sys.stdin = open('3349. 최솟값으로 이동하기.txt','r')

T = int(input())
for tc in range(T):
    W, H, N = map(int,input().split())
    route = list()
    for n in range(N):
        x, y = map(int,input().split())
        route.append((x,y))
    count = 0
    for i in range(1,len(route)):
        sx = route[i-1][0]
        sy = route[i-1][1]
        ex = route[i][0]
        ey = route[i][1]
        while sx != ex or sy != ey:
            if sx > ex and sy > ey:
                sx -= 1
                sy -= 1
                count += 1
            elif sx < ex and sy < ey:
                sx += 1
                sy += 1
                count += 1
            elif sx > ex:
                sx -= 1
                count += 1
            elif sx < ex:
                sx += 1
                count += 1
            elif sy > ey:
                sy -= 1
                count += 1
            elif sy < ey:
                sy += 1
                count += 1
    print('#{} {}'.format(tc+1,count))