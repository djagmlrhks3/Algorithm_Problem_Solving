import sys
sys.stdin=open('5189. 전자카트.txt','r')
"""
1-2-3-1
1-3-2-1
"""
def cart(n, k, sum):
    global result
    if k == n:
        sum += matrix[basic[k-1]][0]
        if result > sum:
            result = sum
    if result < sum:
        return
    else:
        for i in range(k,n):
            basic[k], basic[i] = basic[i], basic[k]
            if k == 0:
                cart(n, k+1, sum+matrix[0][basic[k]])
                basic[k], basic[i] = basic[i], basic[k]
            else:
                cart(n, k+1, sum+matrix[basic[k-1]][basic[k]])
                basic[k], basic[i] = basic[i], basic[k]

T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    basic = [ i for i in range(1,N) ]
    result = 10000000000
    cart(len(basic),0, 0)
    print('#{} {}'.format(tc+1, result))