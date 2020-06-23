import sys
sys.stdin = open('4869. 종이붙이기.txt','r')


def result(n):
    result = [0]*n
    result[0] = 1
    result[1] = 3

    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2] * 2

    return result[n - 1]

T = int(input())
for tc in range(T):
    N = int(input())//10
    print('#{} {}'.format(tc+1,result(N)))