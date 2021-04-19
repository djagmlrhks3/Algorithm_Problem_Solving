def solution(s):
    answer = 0
    for t in range(len(s)):
        temp = s[t:] + s[:t]
        stack = []
        for t in temp:
            if t in '({[':
                stack.append(t)
            elif stack and t == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and  t == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and  t == ']' and stack[-1] == '[':
                stack.pop()
            else:
                break
        else:
            if not stack:
                answer += 1
    return answer