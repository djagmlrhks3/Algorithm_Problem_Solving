import sys
sys.stdin=open('6190. 정곤이의 단조 증가하는 수.txt','r')

T = int(input())
for tc in range(T):
    L = int(input())
    data_list = list(map(str,input().split()))
    result = list()
    for i in range(len(data_list)-1):
        for j in range(i+1,len(data_list)):
            num =int(data_list[i]) * int(data_list[j])
            case = str(num)
            start = True
            for k in range(1, len(case)):
                if case[k-1] > case[k]:
                    start = False
                    break
            if start:
                result.append(num)
    if len(result) > 0:
        result_max = max(result)
        print(f'#{tc+1} {result_max}')
    else:
        print(f'#{tc+1} -1')