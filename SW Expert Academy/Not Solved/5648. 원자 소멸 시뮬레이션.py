import sys
sys.stdin = open('5648. 원자 소멸 시뮬레이션.txt','r')

# T = int(input())
# for tc in range(T):
#     N = int(input()) #원자의 수
#     """
#     x, y : 좌표
#     d : 이동방향 상0, 하1, 좌2, 우3
#     원자들의 보유 에너지 K
#     """
#     d0 = []
#     d1 = []
#     d2 = []
#     d3 = []
#     for _ in range(N):
#         x, y, d, K = map(int,input().split())
#         if d == 0:
#             d0.append((x, y, K))
#         elif d== 1:
#             d1.append((x, y, K))
#         elif d == 2:
#             d2.append((x, y, K))
#         else:
#             d3.append((x, y, K))
#     """
#     -1000,0은 우로 이동 5
#     1000,0은 좌로 이동 3
#     0,1000은 아래로 이동 7
#     0,-1000은 위로 이동 9
#     """
#     print(d0)
#     print(d1)
#     print(d2)
#     print(d3)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def f(N, atom):
    s = 0
    for x in range(4001):
        col = {}
        for i in range(N):
            if atom[i][3] != 0:
                atom[i][0] += dx[atom[i][2]]
                atom[i][1] += dy[atom[i][2]]
                if abs(atom[i][0]) <= 2000 and abs(atom[i][1]) <= 2000:
                    if (atom[i][0], atom[i][1]) not in col:
                        col[(atom[i][0], atom[i][1])] = i
                    else:
                        s += atom[col[(atom[i][0], atom[i][1])]][3]+atom[i][3]
                        atom[i][3] = 0
                        atom[col[(atom[i][0], atom[i][1])]][3] = 0
    return s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom = []
    for i in range(N):
        x, y, d, e = map(int,input().split())
        atom.append([x*2, y*2, d, e])
    ans = f(N, atom)
    print('#{} {}'.format(tc, ans))
