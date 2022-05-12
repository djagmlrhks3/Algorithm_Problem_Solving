import sys
sys.stdin = open('백준10799. 쇠막대기.txt', 'r')

inputs = sys.stdin.readline().rstrip()
stack = []
answer = 0
for i in  range(len(inputs)):
    if inputs[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if inputs[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1
print(answer)