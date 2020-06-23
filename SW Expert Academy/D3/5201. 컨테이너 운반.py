import sys
sys.stdin = open('5201. 컨테이너 운반.txt','r')
"""
트럭이 운반할 수 있는 무게의 컨테이너가 존재하면 해당 컨테이너를 옮기는 것이 최상
그렇지 않을 경우 내림차순으로 정렬한 컨테이너 중 자신보다 작은 값들 중 최대값
"""
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    container = list(map(int,input().split()))
    container.sort(reverse=True)
    truck = list(map(int,input().split()))
    result = 0
    for t in truck:
        if t in container:
            result += t
            container.remove(t)
        else:
            for c in container:
                if t > c:
                    result += c
                    container.remove(c)
                    break
    print('#{} {}'.format(tc+1,result))