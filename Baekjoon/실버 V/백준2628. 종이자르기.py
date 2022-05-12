import sys
sys.stdin = open('백준2628. 종이자르기.txt', 'r')
h, w = map(int, input().split())
width = [0, w]
height = [0, h]
for _ in range(int(input())):
    d, num = map(int, sys.stdin.readline().split())
    if d:
        height.append(num)
    else:
        width.append(num)
height.sort()
width.sort()
max_w, max_h = 0, 0
for i in range(1, len(height)):
    max_h = max(max_h, height[i] - height[i-1])
for i in range(1, len(width)):
    max_w = max(max_w, width[i] - width[i-1])
print(max_w * max_h)