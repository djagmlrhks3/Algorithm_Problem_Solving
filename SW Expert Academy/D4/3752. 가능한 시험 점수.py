import sys
sys.stdin = open('3752. 가능한 시험 점수.txt', 'r')

# def solution(k, total):
#     global N
#     if k == N:
#         if total not in result:
#             result.append(total)
#         return
#     else:
#         solution(k+1, total+data[k])
#         solution(k+1, total)

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    check = [1] + [0]*sum(data)
    for num in data:
        for i in range(len(check)-1,-1,-1):
            if check[i]:
                check[i+num] = 1

    print('#{} {}'.format(tc+1, sum(check)))

