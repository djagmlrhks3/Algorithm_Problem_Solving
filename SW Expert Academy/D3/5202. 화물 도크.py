import sys
sys.stdin = open('5202. 화물 도크.txt','r')
"""
time : 0 ~ 24 시간을 표현하는 리스트
끝나는 시간 - 시작 시간이 최소값인 것부터 배치
"""
T = int(input())
for tc in range(T):
    N = int(input())
    time = [0]*24
    result = 0
    candidate = []
    for n in range(N):
        s, e = map(int,input().split())
        candidate.append((e-s,s,e))
    candidate.sort()
    for i in candidate:
        if sum(time[i[1]:i[2]]) == 0:
            for j in range(i[1],i[2]):
                time[j] += 1
            result += 1
    print('#{} {}'.format(tc+1,result))
