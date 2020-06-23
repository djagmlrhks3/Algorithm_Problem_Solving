import sys
sys.stdin=open('4050. 재관이의 대량 할인.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    input_data = list(map(int,input().split()))
    input_data.sort(reverse=True)
    empty = list()
    result = 0
    for i in input_data:
        empty.append(i)
        if len(empty) == 3:
            result += sum(empty) - min(empty)
            empty.clear()
    if len(empty):
        result += sum(empty)
    print('#{} {}'.format(tc+1,result))