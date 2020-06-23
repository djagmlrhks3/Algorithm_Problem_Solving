import sys
sys.stdin = open('5186. 이진수2.txt', 'r')

def calculate(num):
    global result
    for i in range(13):
        if num == 0:
            break
        num *= 2
        if len(str(num)) > l:
            result += '1'
            num = int(str(num)[1:])
        else:
            result += '0'
    else:
        result = 'overflow'
T = int(input())
for tc in range(T):
    num = input()[2:]
    l = len(num)
    result = ''
    calculate(int(num))
    print('#{} {}'.format(tc + 1, result))
