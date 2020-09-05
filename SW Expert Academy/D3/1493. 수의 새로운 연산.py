import sys
sys.stdin = open('1493. 수의 새로운 연산.txt', 'r')

def find(x, y):
    return x + int((y * (y+1))/2)

def location(num):
    for i in range(1, 150):
        if 1 + (i * (i-1))/2 > num:
            return int((i-1) * (i-2) / 2), i-1
T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    front_x1, front_y = location(p)
    front_x = p - front_x1
    back_x1, back_y = location(q)
    back_x = q - back_x1
    print('#{} {}'.format(tc+1, find(front_x + back_x, front_y + back_y)))
