import sys
sys.stdin = open('2105. 디저트 카페.txt','r')

def chk(n,x,y,stack):
    global result
    if n == 4:
        if x == i and y == j and len(stack) > result:
            result = len(stack)
        else:
            return
    if 0 <= x <= N-1 and 0<= y <= N-1 and matrix[x][y] not in stack:
        chk(n,x+dx[n],y+dy[n],stack+[matrix[x][y]])
        chk(n+1,x+dx[n],y+dy[n],stack+[matrix[x][y]])
    else:
        return
T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    dx = [1,1,-1,-1]
    dy = [-1,1,1,-1]
    result = 0
    for i in range(N-2):
        for j in range(1,N-1):
            chk(0,i,j,[])
    print('#{} {}'.format(tc+1,result)) if result else print('#{} {}'.format(tc+1,-1))

