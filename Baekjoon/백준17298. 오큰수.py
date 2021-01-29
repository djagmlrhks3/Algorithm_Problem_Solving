import sys
sys.stdin = open('백준17298. 오큰수.txt', 'r')
# from collections import deque
# N = int(input())
# numbers = list(map(int, sys.stdin.readline().split()))
# res = [-1]
# used = deque([numbers.pop()])
# while numbers:
#     num = numbers.pop()
#     for idx in range(len(used)):
#         if used[idx] > num:
#             res.append(used[idx])
#             break
#     else:
#         res.append(-1)
#     used.appendleft(num)
# print(' '.join(map(str, res[::-1])))

import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
res = [-1] * N
stack = [0]
idx = 1
while stack and idx < N:
    while stack and numbers[stack[-1]] < numbers[idx]:
        res[stack.pop()] = numbers[idx]

    stack.append(idx)
    idx += 1
print(' '.join(map(str, res)))