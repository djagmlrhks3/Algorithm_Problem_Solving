import sys
sys.stdin = open('1232. 사칙연산.txt','r')

def calculate(li):
    if li[1] == '+':
        li.pop(1)
        num1 = int(li.pop(1))-1
        num2 = int(li.pop(1))-1
        li.append(int(basic[num1][1]) + int(basic[num2][1]))
        return li
    if li[1] == '-':
        li.pop(1)
        num1 = int(li.pop(1))-1
        num2 = int(li.pop(1))-1
        li.append(int(basic[num1][1]) - int(basic[num2][1]))
        return li
    if li[1] == '*':
        li.pop(1)
        num1 = int(li.pop(1))-1
        num2 = int(li.pop(1))-1
        li.append(int(basic[num1][1]) * int(basic[num2][1]))
        return li
    if li[1] == '/':
        li.pop(1)
        num1 = int(li.pop(1))-1
        num2 = int(li.pop(1))-1
        li.append(int(basic[num1][1]) // int(basic[num2][1]))
        return li

T = 10
for tc in range(T):
    N = int(input())
    basic = [0] * (N+1)

    for n in range(1,N+1):
        before = input().split()
        basic[n] = before

    for i in range(N,0,-1):
        if len(basic[i]) > 2:
            before_cal = basic.pop(i)
            basic.insert(i,calculate(before_cal))

    print('#{} {}'.format(tc+1,basic[1][1]))
