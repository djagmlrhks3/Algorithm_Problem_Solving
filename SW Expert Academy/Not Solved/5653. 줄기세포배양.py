import sys
sys.stdin = open('5653. 줄기세포배양.txt','r')
"""
세로크기 N
가로크기 M
배양시간 

출력 : 배양을 K시간 시킨 후 배양용기에 있는 살아잇는 줄기세포(비활성+활성)
"""

dx = [0,0,-1,1]
dy = [-1,1,0,0]
T = int(input())
for tc in range(T):
    N, M, K = map(int,input().split())
    my_map = [list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (M + K) for _ in range(K)]
    # sero = #N
    # matrix = []
    # garo = [0] * ((K//2)+1) #M
    # for n in range(N):
    #     center = list(map(int,input().split()))
    #     center = garo + center + garo
    #     length = len(center)
    #     matrix.append(center)
    # sero = [[0]*length]
    # for m in range(K):
    #     matrix = sero + matrix + sero
    # for i in matrix:
    #     print(i)
    for i in my_map:
        print(i)