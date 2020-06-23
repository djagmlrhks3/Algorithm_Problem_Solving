import sys
sys.stdin = open('5213. 진수의 홀수 약수.txt','r')

# 시간초과가 났을 경우 미리 만들어서 출력하는 방법도 생각해보자

basic = [1]*1000001  # 1은 모든 수의 약수니까 1을 요소로하는 100000+1 길이의 리스트생성
for i in range(3,1000000,2):  # 홀수의 약수를 구하는거니까 3부터 999999까지 +2로 반복
    for j in range(1,(1000000//i)+1):  # i를 약수로 가지려면 곱셈에 i값이 포함되야하고 1000000값을 넘으면 안되니까 최대 범위는 1000000//i 까지 (+1은 리스트에서 마지막값이 -1이니까 추가)
        basic[i*j]+=i  # 해당 인덱스에 i를 더함 (의미 : i*j는 i로 나눠지는 값 즉, i*j는 i를 약수로 가지고 있다.)
for i in range(1,len(basic)):  # 앞에서 구한 리스트에 대해서 미리 합을 구해 둔다. 나중에 for문으로 range(L,R)을반복하면 매번 테스트케이스마다 반복문을 돌리므로 시간초과 발생
    basic[i]+=basic[i-1]

T = int(input())
for tc in range(T):
    result = 0
    L, R = map(int, input().split())
    print('#{} {}'.format(tc+1,basic[R]-basic[L-1]))

    # for i in range(1,10000001):
    #     if i%2:
    #         sum = i
    #         for j in range(3,(i//2)+1,2):
    #             if not i%j:
    #                 sum += j
    #         result.append(sum)
    #     else:
    #         sum = 0
    #         for j in range(3,(i//2)+1,2):
    #             if not i%j:
    #                 sum += j
    #         result.append(sum)