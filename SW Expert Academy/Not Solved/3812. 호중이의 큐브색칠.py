import sys
sys.stdin = open('3812. 호중이의 큐브색칠.txt','r')

T = int(input())
for tc in range(T):
    X,Y,Z,A,B,C,N = map(int,input().split())
    colors = [0]*N
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                colors[(abs(x-A)+abs(y-B)+abs(z-C))%N] +=1
    print('#{}'.format(tc+1),end=" ")
    for i in colors:
        print(i,end=" ")
    print()
