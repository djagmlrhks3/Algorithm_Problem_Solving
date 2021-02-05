import sys
sys.stdin = open('백준16637. 괄호 추가하기.txt', 'r')

def calculate(num1, order, num2):
    if order == '+':
        return num1 + num2
    elif order == '-':
        return num1 - num2
    else:
        return num1 * num2

def move(idx, cnt, flag, orders):
    global count
    if cnt == count:
        candidates.append(orders)
        return
    if flag:
        move(idx+2, cnt+1, False, orders)
    else:
        move(idx, cnt+1, True, orders[:idx-1] + [calculate(orders[idx-1], orders[idx], orders[idx+1])] + orders[idx+2:])
        move(idx+2, cnt+1, False, orders)

order = ['+', '-', '*']
N = int(input())
origin = input()
answer = -0xfffffffff
orders = []
candidates = []
num = ''

for unit in origin:
    if unit not in order:
        num += unit
    else:
        orders.append(int(num))
        orders.append(unit)
        num = ''
orders.append(int(num))

count = len(orders)//2
move(1, 0, False, orders)

for candidate in candidates:
    target = candidate[::-1]
    for i in range(len(candidate)//2):
        target.append(calculate(target.pop(), target.pop(), target.pop()))
    answer = max(answer, target[0])
print(answer)
