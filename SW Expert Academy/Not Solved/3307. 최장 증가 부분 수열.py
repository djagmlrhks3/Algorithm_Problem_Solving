import sys
sys.stdin = open('3307. 최장 증가 부분 수열.txt','r')

# def chk(id,val,count):
#     global max, result
#     if len(val) >= 2 and int(val[-2]) > int(val[-1]):
#         return
#     if id == N-1:
#         if count > max:
#             max = count
#     else:
#         chk(id+1,val+str(input_data[id+1]),count+1)
#         chk(id+1,val,count)
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     input_data = list(map(int,input().split()))
#     max = 0
#     for n in range(N):
#         chk(n,str(input_data[n]),1)
#     print('#{} {}'.format(tc+1,max))

T = int(input())
for tc in range(T):
    N = int(input())
    input_data = list(map(int,input().split()))
    max = 0
    result = list()



