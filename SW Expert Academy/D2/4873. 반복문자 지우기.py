import sys
sys.stdin = open('4873. 반복문자 지우기.txt','r')

def push(item):
    empty.append(item)
def pop():
    if len(empty) == 0:
        return
    else:
        return empty.pop(-1)

T = int(input())
for tc in range(T):
    input_data = input()
    empty = list()
    for i in range(len(input_data)):
        if len(empty) == 0 or empty[-1] != input_data[i]:
            push(input_data[i])
        elif empty[-1] == input_data[i]:
            pop()

    print('#{} {}'.format(tc+1, len(empty)))
