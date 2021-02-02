import sys
sys.stdin = open('백준1002. 터렛.txt', 'r')

def radius(x1, x2, y1, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = radius(x1, x2, y1, y2)
    if not distance:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if abs(r1 - r2) > distance or r1 + r2 < distance:
            print(0)
        elif abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)
        else:
            print(2)
