import sys
sys.stdin = open('백준15685. 드래곤 커브.txt','r')
# matrix =
direction = [(0,1), (-1,0), (0,-1), (0,1)]
def dragon(point,step):
    if step == g+1:
        return
    else:
        for i in dummy:
            i[0] + point_x
            i[1] + point_y

        dragon()
N = int(input())
dummy = set()
for n in range(N):
    dummy = set()
    x, y, d, g = map(int,input().split())
    point_x = x + direction[d][0]
    point_y = y + direction[d][1]
    dummy.add((x,y))
    dragon(point_x,point_y,0)
    print(dummy)