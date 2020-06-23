import sys
sys.stdin=open('1220. Magnetic.txt','r')

for tc in range(10):
    N=int(input())
    matrix = list()
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    count = 0
    for j in range(100):
        sample = list()
        for i in range(100):
            if matrix[i][j]:
                sample.append(matrix[i][j])
        S = list()
        for i in sample:
            if i == 2:
                if len(S):
                    count += 1
                    S.clear()
                else:
                    continue
            else:
                S.append(i)
    print('#{} {}'.format(tc+1,count))

