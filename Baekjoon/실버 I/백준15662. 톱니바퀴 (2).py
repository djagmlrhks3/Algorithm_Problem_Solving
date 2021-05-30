import sys
sys.stdin = open('백준15662. 톱니바퀴 (2).txt', 'r')

def clock(idx):
    pick = topni[idx].pop()
    topni[idx].insert(0, pick)

def anticlock(idx):
    pick = topni[idx].pop(0)
    topni[idx].append(pick)

def left(idx,value,d):
    if idx < 0:
        return
    else:
        if topni[idx][2] == value:
            return
        else:
            if d==1:    #시계방향
                anticlock(idx)
                left(idx-1,topni[idx][5], -d)
            else:       #반시계방향
                clock(idx)
                left(idx-1,topni[idx][7], -d)
def right(idx,value, d):
    if idx > cnt-1:
        return
    else:
        if topni[idx][6] == value:
            return
        else:
            if d==1:    #시계방향
                anticlock(idx)
                right(idx+1, topni[idx][1], -d)
            else:       #반시계방향
                clock(idx)
                right(idx+1, topni[idx][3], -d)

def circle(n, d):
    if d == 1:
        clock(n)
        left(n-1, topni[n][7], d)
        right(n+1, topni[n][3], d)
    else:
        anticlock(n)
        left(n-1, topni[n][5], d)
        right(n+1, topni[n][1], d)

cnt = int(sys.stdin.readline().rstrip())
topni = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(cnt)]
K = int(input())
for k in range(K):
    n, d = map(int, sys.stdin.readline().split())
    circle(n-1, d)

result = 0
for t in topni:
    result += t[0]
print(result)