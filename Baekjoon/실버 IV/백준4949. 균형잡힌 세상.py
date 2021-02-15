import sys
sys.stdin = open('백준4949. 균형잡힌 세상.txt', 'r')
sb = '([])'
while True:
    stack = []
    sentence = input().rstrip()
    if sentence == '.':
        break
    for word in sentence:
        if word in sb:
            if word == '(' or word == '[':
                stack.append(word)
            elif word == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    print("no")
                    break
            elif word == "]":
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    print("no")
                    break
    else:
        if stack: print("no")
        else: print("yes")


