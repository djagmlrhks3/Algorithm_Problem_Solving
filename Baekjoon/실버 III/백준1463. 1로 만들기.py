import sys
sys.stdin = open('백준1463. 1로 만들기.txt', 'r')

X = int(input())
d = [0] * (10**6 + 1)

for i in range(2, X+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[X])

# from _collections import deque
# numbers = deque([[X, 0]])
# visited = [X]
# ans = 0
# while True:
#     num, time = numbers.popleft()
#     if not num % 3:
#         if num//3 == 1:
#             ans = time
#             break
#         if num//3 not in visited:
#             visited.append(num//3)
#             numbers.append((num//3, time+1))
#     if not num % 2:
#         if num//2 == 1:
#             ans = time
#             break
#         if num//2 not in visited:
#             visited.append(num//2)
#             numbers.append((num//2, time+1))
#     if num-1 == 1:
#         ans = time
#         break
#     if num-1 not in visited:
#         visited.append(num-1)
#         numbers.append((num-1, time+1))

# print(time+1)