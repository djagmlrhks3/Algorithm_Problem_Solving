import sys
sys.stdin = open('5431. 민석이의 과제 체크하기.txt','r')

T = int(input())
for tc in range(T):
    N, K = map(int,input().split())
    input_data = list(map(int,input().split()))
    student = [0]*(N+1)
    for i in input_data:
        student[i] += 1
    print('#{}'.format(tc+1), end=" ")
    for i in range(1,N+1):
        if student[i] == 0:
            print(i, end=" ")
    print()
