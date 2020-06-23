import sys
sys.stdin = open('백준16637. 괄호 추가하기.txt', 'r')
orders = ['+','-','*']

def solution(idx, total):
    global result
    if idx == N:
        result = max(result, total)
        return
    num = number[idx+1]
    pmm = order[idx]
    if pmm == '+':
        solution(idx+1, total+number[idx+1])
        if idx == N:return
        num = number[idx+1]
        pmm = order[idx+1]
        if pmm == '+':
            solution(idx+1, total+num)
        elif pmm == '-':
            solution(idx+1, total-num)
        else:
            solution(idx+1, total*num)
    elif pmm == '-':
        solution(idx+1, total-number[idx+1])
        if idx == N:return
        num = number[idx+1]
        pmm = order[idx+1]
        if pmm == '+':
            solution(idx+1, total+num)
        elif pmm =='-':
            solution(idx+1, total-num)
        else:
            solution(idx+1, total*num)
    else:
        solution(idx+1, total*number[idx+1])
        if idx == N:return
        num = number[idx+1]
        pmm = order[idx+1]
        if pmm == '+':
            solution(idx+1, total+num)
        elif pmm == '-':
            solution(idx+1, total-num)
        else:
            solution(idx+1, total*num)

N = int(input())
data = input()
number = list()
order = list()
result = 0
for i in range(len(data)):
    order.append(data[i]) if i%2 else number.append(int(data[i]))

solution(0, number[0])