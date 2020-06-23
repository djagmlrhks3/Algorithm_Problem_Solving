import sys
sys.stdin = open('5188. 최소합.txt','r')

def check(i,j,total):
    global result
    if i > N-1 or j > N-1:
        return
    if total > result:    #가지치기
        return
    if i==N-1 and j==N-1:
        total += matrix[N-1][N-1]
        if total < result:
            result = total
            return
    else:
        check(i+1,j,total+matrix[i][j])
        check(i,j+1,total+matrix[i][j])

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    total = 0
    result = 10000000
    check(0,0,0)
    # for i in matrix:
    #     print(i)
    print('#{} {}'.format(tc+1,result))

