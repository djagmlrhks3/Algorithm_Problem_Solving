import sys
sys.stdin = open('3809. 화섭이의 정수 나열.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    input_data = list()
    while len(input_data) < N:
        empty = list(input().split())
        input_data += empty
    number = str("".join(input_data))
    for i in range(10**3+1):
        if number.find(str(i))<0:
            result = i
            break
    print('#{} {}'.format(tc+1,result))



