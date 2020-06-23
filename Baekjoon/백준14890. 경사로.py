import sys
sys.stdin = open('백준14890. 경사로.txt','r')
"""
파인만 알고리즘
일단, L보다 작은 연속된 수가 있으면 X
하나씩 탐색하면서
첫 번 째 값을 저장
이전 과 같으면 legth + 1

다른 값이 나왔는데
자기보다 작으면
자기보다 크면
if length < L or 차이가 2 이상이면 False
if length > L or 차이가 1이면 대소비교


"""
N, L = map(int,input().split())
mountain = [list(map(int,input().split())) for _ in range(N)]
count = 0
def check(mountain):
    global count
    for route in mountain:
        chk = list()
        for i in range(N):
            if i == 0:  # 첫 번째 값 저장
                last = route[i]
                length = 1
            else:
                if abs(last-route[i])>=2 and not len(chk): #이전 값 보다 2이상 크면 False
                    False
                elif last+1 == route[i]: #이전보다 큰 값
                    if length >= L:
                        last = route[i]
                        length = 1
                    else:
                        break
                elif last == route[i]+1: #이전보다 작은 값
                    if not len(chk):     #최소 L만큼의 개수가 앞으로 나와야 되니까 리스트에 담아서 개수 확인
                        chk.append(route[i]) #처음으로 이전보다 작은 값이 나오면 list에 추가하고 1로 초기화
                        length = 1
                    else:
                        if chk[-1] == route[i]:
                            chk.append(route[i])
                        elif chk[-1] == route[i]+1:
                            if len(chk) >= L:
                                chk.clear()
                                chk.append(route[i])
                                length = 1
                            else:
                                break
                        else:
                            break
                elif last == route[i]: #같은 높이가 나올 경우
                    if len(chk):
                        if len(chk) < L:
                            break
                        else:
                            chk.clear()
                            length = 1
                    else:
                        length += 1

        count += 1

check(mountain)
check(list(zip(*mountain)))
